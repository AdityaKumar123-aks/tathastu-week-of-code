# TAKING RUNS OF THREE PLAYERS AND FIND FOLLOWING:
# * STRIKE RATE OF EACH
# * WHAT WILL BE THE RUNS SCORE IF THEY PLAYED 60 BALLS MORE?
# * WHAT IS THE MAX. NO. OF SIXES EACH PLAYER COULD HAVE HIT?

a=int(input("runs of I player :"))
b=int(input("runs of II player :"))
c=int(input("runs of III player :"))
print("strike rate of I player :",(a*100)/60)
print("strike rate of II player :",(b*100)/60)
print("strike rate of III player :",(c*100)/60)
print("new score of I player :",a*2)
print("new score of II player :",b*2)
print("new score of III player :",c*2)
print("max.no.of sixes I player could have hit :",a//6)
print("max.no.of sixes II player could have hit :",b//6)
print("max.no.of sixes III player could have hit :",c//6)
