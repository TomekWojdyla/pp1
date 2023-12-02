#open('stuff.txt')
#stuff = "Witaj\nŚwiecie!"
#print(stuff)

fout=open('output.txt','w')
print(fout)
line1='oto galaz eukaliptusa\n'
fout.write(line1)
line2='ojczyzny naszej emblemat\n'
fout.write(line2)
fout.close()

