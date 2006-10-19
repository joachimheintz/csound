import CsoundVST
import math
import random

print 'UNIT TESTS FOR CsoundVST.Voicelead and CsoundVST.Score'
print

for i in xrange(36, 96, 1):
    p = float(i)
    print '%8.3f = Voicelead_pc(%8.3f)' % (CsoundVST.Voicelead_pc(p), p)
print
a = [0, 4, 7, 11]
b = [1, 5, 8,  0]
print '%s = Voicelead_voiceleading(%s, %s)' % (CsoundVST.Voicelead_voiceleading(a, b), a, b)
print
c = [5, 5, 5, 5]
print '%s = Voicelead_areParallel(%s, %s)' % (CsoundVST.Voicelead_areParallel(a, b), a, b)
print '%s = Voicelead_areParallel(%s, %s)' % (CsoundVST.Voicelead_areParallel(a, c), a, c)
print
print '%s = Voicelead_rotate(%s)' % (CsoundVST.Voicelead_rotate(a), a)
print
rotations = CsoundVST.Voicelead_rotations(a)
print '%s = CsoundVST.Voicelead_rotations(%s)' % (a, rotations)
for chord in rotations:
    print chord
print
pitches = [65., 69., 72., 76.]
print '%s = Voicelead_pcs(%s)' % (CsoundVST.Voicelead_pcs(pitches), pitches)
print '%8.3f = Voiclead_numberFromChord(%s)' % (CsoundVST.Voicelead_numberFromChord(pitches), pitches)
print '%8.3f = Voiclead_numberFromChord(%s)' % (CsoundVST.Voicelead_numberFromChord(a), a)
print
print '%s = Voicelead_pcsFromNumber(%8.3f)' % (CsoundVST.Voicelead_pcsFromNumber(2193), 2193)
print
voicings = CsoundVST.Voicelead_voicings(a, 36, 60)
print 'Voicelead_voicings(%s, %s, %s):' % (a, 36, 60)
for chord in voicings:
    print chord
print
CM7 = [60., 64., 67., 71.]
print 'CM7: %s' % (CM7)
FM7 = [65., 69., 72., 76.]
print 'FM7: %s' % (FM7)
G7 =  [67., 71., 74., 77.]
print 'G7:  %s' % (G7)
t1 = CsoundVST.Voicelead_voicelead(CM7, FM7, 0., 96., False)
print '%s = CsoundVST.Voicelead_voicelead(%s, %s, 0, 96., True)' % (t1, CM7, FM7)
t2 = CsoundVST.Voicelead_voicelead(t1, G7, 0., 96., False)
print '%s = CsoundVST.Voicelead_voicelead(%s, %s, 36., 96., True)' % (t2, t1, G7)
print
for i in xrange(36, 96, 1):
	print '%8.3f = Voiclead_closestPitch(Voicelead_pc(%d), %s)' %(CsoundVST.Voicelead_closestPitch(i, CM7), i, CM7)
print
for i in xrange(36, 96, 1):
	print '%8.3f = Voiclead_conformToPitchClassSet(%d, %s)' %(CsoundVST.Voicelead_conformToPitchClassSet(i, a), i, a)
print
score = CsoundVST.Score()
for i in xrange(2000):
	time = i * 0.125
	duration = 0.5
	key = random.randint(36, 96)
	velocity = 80.0
	score.append(time, duration, 144.0, 1.0, key, velocity)
score.save('CsoundVstUnitTest.py.1.mid')
score.setPitchClassSet(0, len(score), a)
score.save('CsoundVstUnitTest.py.2.mid')
pcsI = CsoundVST.Voicelead_numberFromChord([0.,4.,7.,11.,14.]) - 1.0
for i in xrange(0, len(score), 20):
	pcsI = pcsI + 5.0
	pcsI = pcsI % 4095
	pcsN = pcsI + 1
	CsoundVST.Voicelead.pcsFromNumber(pcsN)
	score.setPitchClassSet(i, i + 20, CsoundVST.Voicelead_pcsFromNumber(pcsN, 12), 12)
score.save('CsoundVstUnitTest.py.3.mid')
for i in xrange(0, len(score), 20):
	pcs = CsoundVST.Voicelead_pcs(score.getPitches(i, i + 20))
	#print pcs
	score.voicelead(i, i + 20, i + 20, i + 40, True)
score.save('CsoundVstUnitTest.py.4.mid')

	




	
	


























