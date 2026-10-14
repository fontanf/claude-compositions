"""Doigtés de main gauche à partir de la répartition corde/case trouvée par le vérificateur.

Règles :
- une position par forme (demi-mesure) dans les arpèges, une par attaque dans les passages en ligne ;
- un doigt par case à partir de la case la plus basse ; barré (doigt 1) quand plusieurs notes partagent la
  case la plus basse sans corde à vide entre elles ;
- on note le doigt et la corde (chiffre cerclé) à la première apparition de chaque note dans la position ;
  les cordes à vide ne sont pas marquées.
"""
import re
from fractions import Fraction as F

ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII",
         "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"]


def fingers(sf):
    """sf : ensemble de (corde, case). -> {(corde, case): doigt}, barré éventuel (case, nb de cordes)"""
    fretted = sorted({(f, s) for s, f in sf if f > 0})
    if not fretted:
        return {}, None
    lo = fretted[0][0]
    opens = {s for s, f in sf if f == 0}
    res, barre, nxt = {}, None, 1
    group = [s for f, s in fretted if f == lo]
    rest = fretted
    if len(group) >= 2 and not any(min(group) < o < max(group) for o in opens):
        for s in group:
            res[(s, lo)] = 1
        barre, nxt = (lo, max(group) - min(group) + 1), 2
        rest = [(f, s) for f, s in fretted if f > lo]
    for f, s in rest:
        fin = min(4, max(nxt, f - lo + 1))
        res[(s, f)] = fin
        nxt = min(4, fin + 1)
    return res, barre


def needs_string(p, sf, tuning):
    """on n'indique la corde que si la note n'est pas jouée à sa case la plus basse possible"""
    lowest = min(p - o for o in tuning if p - o >= 0)
    return sf[1] > lowest


def assign_forme(t, base, mels, tuning):
    """répartition cohérente : la forme (basse + arpège) est fixée, puis chaque note de mélodie s'y ajoute"""
    bp = sorted({p for n in base for p in n["pitches"]})
    first = mels[0]["pitches"] if mels else []
    sol = t.solve(bp + list(first))
    if sol is None:
        return None
    fixed = {p: sol[p] for p in bp}
    out = {(id(n), p): fixed[p] for n in base for p in n["pitches"]}
    for m in mels:
        used = {s for s, _ in fixed.values()}
        for p in m["pitches"]:
            best = None
            for s in range(6):
                f = p - tuning[s]
                if s in used or not 0 <= f <= t.MAX_FRET:
                    continue
                ok, span = t.feasible(list(fixed.values()) + [(s, f)])
                if ok and (best is None or (span, f) < best[0]):
                    best = ((span, f), (s, f))
            if best:
                out[(id(m), p)] = best[1]
    return out


def annotate(t, data):
    """renvoie des copies de V1 et V2 avec les doigtés"""
    notes = t.all_notes()
    _, strings = t.check(notes=notes)
    starts, _ = t.bar_starts()
    window = getattr(data, "WINDOW", F(3, 8))
    marks = {}          # id(note) -> {pitch: suffixe}
    barres = {}         # id(note) -> texte du barré
    for b in range(1, data.NBARS + 1):
        length = F(data.METER[b][0]).limit_denominator(8)
        b0 = starts[b]
        if data.MODE[b] == "forme_inutilisee":
            for h in range(int(length / window)):
                w0, w1 = b0 + window * h, b0 + window * (h + 1)
                base = [n for n in notes if n["voice"] == 2 and w0 <= n["start"] < w1 and not n["harmonic"]]
                mels = [n for n in notes if n["voice"] == 1 and w0 <= n["start"] < w1 and not n["harmonic"]]
                held = [n for n in notes if n["voice"] == 1 and n["start"] < w0 < n["start"] + n["dur"]]
                asg = assign_forme(t, base, held + mels, data.TUNING)
                if not asg:
                    continue
                fing, barre = fingers(set(asg.values()))
                seen = set()
                for n in sorted(base + mels, key=lambda n: n["start"]):
                    for p in n["pitches"]:
                        sf = asg.get((id(n), p))
                        if sf and sf[1] > 0 and p not in seen and sf in fing:
                            marks.setdefault(id(n), {})[p] = (fing[sf], 6 - sf[0], needs_string(p, sf, data.TUNING))
                            seen.add(p)
                if barre and mels:
                    barres[id(mels[0])] = barre
        else:
            prev_sig = {}
            for tt in sorted({n["start"] for n in notes if b0 <= n["start"] < b0 + length}):
                snd = [n for n in notes if n["start"] <= tt < n["start"] + n["dur"] and not n["harmonic"]]
                sf = {strings[(id(n), k)] for n in snd for k in range(len(n["pitches"])) if (id(n), k) in strings}
                fing, barre = fingers(sf)
                for n in snd:
                    if n["start"] != tt or len(n["pitches"]) == 1:
                        continue  # les notes seules sont doigtées plus bas, par positions
                    sig = tuple(sorted(n["pitches"]))
                    if prev_sig.get(n["voice"]) == sig and len(sig) > 1:
                        continue  # accord répété : doigté déjà indiqué
                    prev_sig[n["voice"]] = sig
                    for k, p in enumerate(n["pitches"]):
                        a = strings.get((id(n), k))
                        if barre and a and a[1] == barre[0] and barre[1] >= 4:
                            continue  # couvert par le barré indiqué « C »
                        if a and a[1] > 0 and a in fing:
                            show = needs_string(p, a, data.TUNING) and n["forced"][k] is None
                            marks.setdefault(id(n), {})[k] = (fing[a], 6 - a[0], show)
                    if barre and barre[1] >= 2 and len(n["pitches"]) > 1:
                        barres[id(n)] = barre
    # passages en ligne : notes seules regroupées en positions de quatre cases au plus
    for b in range(1, data.NBARS + 1):
        if data.MODE[b] == "forme":
            continue
        for voice in (1, 2):
            seq = [n for n in notes if n["bar"] == b and n["voice"] == voice and len(n["pitches"]) == 1
                   and not n["harmonic"] and (id(n), 0) in strings]
            seq = [n for n in sorted(seq, key=lambda n: n["start"]) if strings[(id(n), 0)][1] > 0]
            i = 0
            while i < len(seq):
                j, lo, hi = i, None, None
                while j < len(seq):
                    f = strings[(id(seq[j]), 0)][1]
                    nlo, nhi = min(f, lo or f), max(f, hi or f)
                    if nhi - nlo > 3:
                        break
                    lo, hi, j = nlo, nhi, j + 1
                for n in seq[i:j]:
                    p = n["pitches"][0]
                    sf = strings[(id(n), 0)]
                    show = needs_string(p, sf, data.TUNING) and n["forced"][0] is None
                    marks.setdefault(id(n), {})[0] = (sf[1] - lo + 1, 6 - sf[0], show)
                i = j
    return rewrite(t, data, notes, marks, barres)


def rewrite(t, data, notes, marks, barres):
    by_tok = {(n["voice"], n["bar"], n["tok"]): n for n in notes}
    out = []
    for voice, bars in ((1, data.V1), (2, data.V2)):
        new, last_label = {}, None
        for b in range(1, data.NBARS + 1):
            toks = re.findall(r"<[^>]+>\S*|\S+", bars[b])
            for k, tok in enumerate(toks):
                n = by_tok.get((voice, b, k))
                if n is None or id(n) not in marks:
                    continue
                m = t.TOKEN.match(tok)
                pitch, den, dot, mul, post = m.groups()
                fm = marks[id(n)]

                d = "-" if voice == 1 else "_"   # voix grave : doigtés sous la portée

                def suffix(k):
                    if k not in fm:
                        return ""
                    f, s, show = fm[k]
                    return f"{d}{f}" + (f"{d}\\{s}" if show else "")
                dur = den + dot + (f"*{mul}" if mul else "")
                if pitch.startswith("<"):
                    inner = " ".join(x if "harmonic" in x else x + suffix(k) for k, x in enumerate(pitch[1:-1].split()))
                    head = f"<{inner}>" + dur
                else:
                    head = pitch + dur + suffix(0)
                if id(n) in barres:
                    fret, nstr = barres[id(n)]
                    label = ("C" if nstr >= 4 else "½C") + " " + ROMAN[fret]
                    if label != last_label:  # n'indiquer le barré que lorsqu'il change
                        post = post + f'^"{label}"'
                    last_label = label
                elif id(n) in marks:
                    last_label = None
                toks[k] = head + post
            new[b] = " ".join(toks)
        out.append(new)
    return out
