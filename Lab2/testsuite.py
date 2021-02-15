import III as default
import mutant1 as m1
import mutant2 as m2
import mutant3 as m3
import mutant4 as m4
import mutant5 as m5
import mutant6 as m6
#from https://pypi.org/project/func-timeout/
from func_timeout import func_timeout, FunctionTimedOut



#Probably the ugliest thing I've written in quite some time. 
def runtests(f, testType): 
    testcaseCounter = 0
    m1Wrong = False
    m2Wrong = False
    m3Wrong = False
    m4Wrong = False
    m5Wrong = False
    m6Wrong = False
    for line in f:
        testcase = list(eval(line))
        key = testcase[0]
        array = testcase[1]
        correctAnswer = default.III(key, array)
        #print(line)
        #print(correctAnswer)
        if not m1Wrong: 
            try:
                m1Answer = func_timeout(0.02, m1.IIImutant1, args=(key, array))
                if m1Answer != correctAnswer:
                    print("m1 error found at testcase: " + str(testcaseCounter) + " Type: " + testType)
                    m1Wrong = True

            except FunctionTimedOut:
                print("m1 timed out with testcase: " + str(testcaseCounter) + " Type: " + testType)

        if not m2Wrong:
            try:
                m2Answer = func_timeout(0.02, m2.IIIMutant2, args=(key, array))
                if m2Answer != correctAnswer:
                    print("m2 error found at testcase: " + str(testcaseCounter)+ " Type: " + testType)
                    m2Wrong = True
            except FunctionTimedOut:
                print("m2 timed out with testcase: " + str(testcaseCounter)+ " Type: " + testType)
        
        if not m3Wrong:
            try:
                m3Answer = func_timeout(0.02, m3.IIIMutant3, args=(key, array))
                if m3Answer != correctAnswer:
                    print("m3 error found at testcase: " + str(testcaseCounter)+ " Type: " + testType)
                    m3Wrong = True
            except FunctionTimedOut:
                print("m3 timed out with testcase: " + str(testcaseCounter)+ " Type: " + testType)
            
        if not m4Wrong:
            try:
                m4Answer = func_timeout(0.02, m4.III, args=(key, array))
                if m4Answer != correctAnswer:
                    print("m4 error found at testcase: " + str(testcaseCounter)+ " Type: " + testType)
                    m4Wrong = True
            except FunctionTimedOut:
                print("m4 timed out with testcase: " + str(testcaseCounter)+ " Type: " + testType)  
        
        if not m5Wrong:
            try:
                m5Answer = func_timeout(0.02, m5.III, args=(key, array))
                if m5Answer != correctAnswer:
                    print("m5 error found at testcase: " + str(testcaseCounter)+ " Type: " + testType)
                    m5Wrong = True
            except FunctionTimedOut:
                print("m5 timed out with testcase: " + str(testcaseCounter)+ " Type: " + testType)
        
        if not m6Wrong:
            try:
                m6Answer = func_timeout(0.02, m6.III, args=(key, array))
                if m6Answer != correctAnswer:
                    print("m6 error found at testcase: " + str(testcaseCounter)+ " Type: " + testType)
                    m6Wrong = True
            except FunctionTimedOut:
                print("m6 timed out with testcase: " + str(testcaseCounter) + " Type: " + testType)

        testcaseCounter += 1
        
        
        

with open('pairwiseTestFile.txt') as f:
    runtests(f, "Pairwise")


with open('randomTestFile.txt') as f:
    runtests(f, "Random")
    





