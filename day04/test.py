things = ['macbook', 'money', 'history']
new = sorted(things)
print(things)
print(new)

fruits=("apple","banana","Pear")

student_info={
    "name" : "Dilwar",
    "Roll NO" : 15,
    "City" : "Mumbai"   
}
print( student_info["City"])
student_info["Grade"] = 'A'
print(student_info)
# print(student_info["age"])
print(student_info.get("age",0))

for key , value in student_info.items():
    print(key ,value)


set1={2,1,3,4,}
set2={3,6,7,8,4,2}
print(set1 | set2)
print(set1 & set2)

print([x*2 for x in range(5)])

print([x*x for x in range(1,11) if x%2==0])
print({x : x**2 for x in range(5)})

from collections import Counter
text = "hello world"
print(Counter(text))


from collections import defaultdict
d = defaultdict(int)
d["count"] += 1
print(d["count"])
print(d["missing"])
sentence = "the cat sat on the mat the cat"
words=sentence.split()
for word in words:
    d[word] += 1
    
print(d)
