## 迪摩根定理
您可以發現  -(x｜y) 和 -x&-y 兩者的真值是一樣的，-(x&y) 與 (-x｜-y) 兩者的真值也是一樣的。
因此、我們得到下列兩個定理：

-(x｜ y) = -x & -y
-(x & y) = -x｜-y
## 謂詞邏輯 (Predicate Logic)
在布林邏輯中，只有用來代表真假值的簡單變數，像是 A, B, C, X, Y, Z .... 等，所以邏輯算式看來通常如下：

P & (P=>Q) => Q.
A & B & C => D | E.
-(A & B) <=> -A | -B.

這種布林命題邏輯裏沒有函數的概念，只有簡單的命題 (Proposition)，因此布林邏輯也稱為命題邏輯 (Propositional Logic)。
而在《謂詞邏輯》(Predicate logic) 裏，則有「布林函數」的概念，因此其表達能力較強，例如以下是一些謂詞邏輯的範例。

Parent(x,y) <= Father(x,y).
Parent(John, Johnson).
Ancestor(x,y) <= Parent(x,y).
Ancestor(x,y) <= Ancestor(x,z) & Parent(z,y).

您可以看到在這種邏輯系統裏，有「布林變數」的概念 (像是 x, y, z 等等)，也有函數的概念，像是 Parent(), Father(), Ancestor() 等等。

一階邏輯(First-Order Logic)
在上述這種謂詞邏輯系統中，如果我們加上 ∀\forall∀ (對於所有) 或 ∃\exists∃ (存在) 這兩個變數限定符號，而其中的謂詞不可以是變項，而必須要是常項，這種邏輯就稱為一階邏輯。


∀People(x)=>Mortal(x)\forall People(x) => Mortal(x)∀People(x)=>Mortal(x) ; 人都是會死的。

People(Socrates)People(Socrates)People(Socrates) ; 蘇格拉底是人。

Mortal(Socrates)Mortal(Socrates)Mortal(Socrates) ; 蘇格拉底會死。

當然、規則可以更複雜，像是以下這個範例，就說明了「存在一些人可以永遠被欺騙」。

∃x(Person(x)∧∀y(Time(y)=>Canfool(x,y))).\exists x (Person(x) \wedge \forall y (Time(y) => Canfool(x,y))).∃x(Person(x)∧∀y(Time(y)=>Canfool(x,y))).


二階邏輯 (Second-Order Logic)
如果一階邏輯中的謂詞，放寬成可以是變項的話 (這些變項可以加上 ∀\forall∀ 與 ∃\exists∃ 等符號的約束)，那就變成了二階邏輯，以下是一些二階邏輯的規則範例。

∃P(P(x)∧P(y)).\exists P (P(x) \wedge P(y)).∃P(P(x)∧P(y)).
∀P∀x(x∈P∣x∉P).\forall P \forall x (x \in P | x \notin P).∀P∀x(x∈P∣x∈/P).
∀P(P(0)∧∀y(P(y)=>P(succ(y)))=>∀yP(y)).\forall P (P(0) \wedge \forall y( P(y)=>P(succ(y)) ) => \forall y P(y) ).∀P(P(0)∧∀y(P(y)=>P(succ(y)))=>∀yP(y)).

(最後一條是《數學歸納法》規則)
對於上述這些邏輯系統而言，描述能力愈強大者，通常也愈複雜，而且《公理系統》與《推論的複雜度》也會提高，要建構出《很完美的數學體系》，難度也就愈來愈高了！