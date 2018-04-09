#! /usr/bin/env python

import random
from collections import Counter
from unit import Unit

random.seed(42)

N = 5000
PRECISION = 3

necron = Unit("NecronWarrior", 5, 3, 3, 4, 4, 1, 10, 4)
tau    = Unit("TauFireWarrior", 6, 5, 4, 5, 3, 1, 6, 4, 6)

def D6(n):
    return [random.randint(1,6) for i in range(n)]

def Simulate(n, attacker, defender, squad, nAttack, ap):
    results = Counter()

    print "Squad of {0}x {1} attacking {2}".format(squad, attacker.Name, defender.Name)
    toWoundMin = defender.toWound(attacker.S)
    toNormalSave = defender.Sv + abs(ap)
    toSaveMin  = min(toNormalSave, defender.ISv)
    if defender.ISv:
        print "{0}+ to wound and {1}+/{2}++ to save".format(toWoundMin, toNormalSave, defender.ISv)
    else:
        print "{0}+ to wound and {1}+ to save".format(toWoundMin, toNormalSave, defender.ISv)
    for i in range(n):
        toHit = D6(squad * nAttack)
        nHit = sum(1 for h in toHit if h >= attacker.BS)
        toWound = D6(nHit)
        nWound = sum(1 for w in toWound if w >= toWoundMin)
        toSave = D6(nWound)
        nUnsaved = sum(1 for s in toSave if (s-ap) < defender.Sv)
        res = (nHit, nWound, nUnsaved)
        results[res] += 1
    return results

def DisplaySim( results, squad ):
    hits = []
    wounds = []
    unsaved = []
    for (h, w, u), ct in results.iteritems():
        for i in range(ct):
            hits.append(h)
            wounds.append(w)
            unsaved.append(u)
    hits = sorted(hits)
    wounds = sorted(wounds)
    unsaved = sorted(unsaved)

    lcb = int(0.025 * N)
    ucb = int(0.975 * N)

    avgHits = round(sum(hits) / float(N), PRECISION)
    avgHitsPer = round(avgHits / squad, PRECISION)
    print "Hits:    {0}/{1} per model (95% CI {2}-{3})".format(avgHits, avgHitsPer, hits[lcb], hits[ucb])
    avgWounds = round(sum(wounds) / float(N), PRECISION)
    avgWoundsPer = round(avgWounds / squad, PRECISION)
    print "Wounds:  {0}/{1} per model (95% CI {2}-{3})".format(avgWounds, avgWoundsPer, wounds[lcb], wounds[ucb])
    avgUnsaved = round(sum(unsaved) / float(N), PRECISION)
    avgUnsavedPer = round(avgUnsaved / squad, PRECISION)
    print "Unsaved: {0}/{1} per model (95% CI {2}-{3})".format(avgUnsaved, avgUnsavedPer, unsaved[lcb], unsaved[ucb])

print
r1 = Simulate(N, necron, tau, 15, 1, 1)
DisplaySim( r1, 15 )
print
r1 = Simulate(N, necron, tau, 15, 2, 2)
DisplaySim( r1, 15)
print
r2 = Simulate(N, tau, necron, 15, 1, 0)
DisplaySim( r2, 15 )
