import sys</code>

<code>netAmount = 0</code>

<code>while True:</code>

<code>    s = input("Nhập nhật ký giao dịch: ")</code>

<code>    if not s:</code>

<code>        break</code>

<code>    values = s.split(" ")</code>

<code>    operation = values[0]</code>

<code>    amount = int(values[1])</code>

<code>    if operation=="D":</code>

<code>         netAmount+=amount</code>

<code>    elif operation=="W":</code>

<code>        netAmount-=amount</code>

<code>    else:</code>

<code>        pass</code>
