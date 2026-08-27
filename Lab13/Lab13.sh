#Question 1(i)
sed -n '/and/p' question1.txt
#1(ii)	
sed 's/language/lang/g' question1.txt
#1(iii)
sed '/is/d' question1.txt
#1(iv)
sed '=' question1.txt | sed 'N;s/\n/ /'
#1(v)
sed '1,2d' question1.txt
#1(vi)
sed-n '1~2p' question1.txt
#1(vii)
sed 's/Python/python/;s/language/lang/' lab13.txt

#Question 2(i)
awk '$2<25 {print $0}' question2.txt
#2(ii)
awk '$3=="physics" {print $0}' question2.txt
#2(iii)
awk '{print $1 "," $2 "," $3 ","}' question2.txt

#Question 3(i)
awk '!/>/' question3.txt
#3(ii)
sed 's/T/U/g' question3.txt
#3(iii)
sed 's/seq1/human_gene/' question3.txt

#Question 4
awk '$4=="PHE"' 1HKO.pdb | awk '{print $2}' > PHE_atoms.xyz:
