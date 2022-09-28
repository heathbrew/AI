TESTpos =  99
TESTneg = 99
TESTndandneg = 1
totalcase = 10000
#totalp = 100
TESTndandneg = totalcase - (TESTpos + TESTneg+TESTndandneg)
A = TESTpos/totalcase
B = (TESTpos+TESTneg)/totalcase
prob_b_a = (TESTpos/totalcase)/A
prob_a_b = (prob_b_a*A)/B
print(prob_a_b*100,"%")