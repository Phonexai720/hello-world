s = input("Nhập câu của bạn: ")</code>
<code>d={"UPPER CASE":0, "LOWER CASE":0}</code>

<code>for c in s:</code>

<code>    if c.isupper():</code>

<code>        d["UPPER CASE"]+=1</code>

<code>    elif c.islower():</code>

<code>        d["LOWER CASE"]+=1</code>

<code>    else:</code>

<code>        pass</code>

<code>print ("Chữ hoa:", d["UPPER CASE"])</code>

<code>print ("Chữ thường:", d["LOWER CASE"])
