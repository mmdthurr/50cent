#!/home/mmd/code/50cent/env/bin/python


import requests



r = requests.get("https://api.nobitex.ir/market/stats?srcCurrency=usdt")
d = r.json()["stats"]["usdt-rls"]["bestSell"]


base_html = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> 50 Cent - %{d}% Toman</title>
    <style>
        div {
            max-width: 500px;
            margin: auto;
        }

        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            min-width: 300px;
            width: 100%;
        }
    </style>

</head>

<body>
    <div>
        <div>
            <img src="/50cent.jpg" alt="">
            <p style="direction: rtl;white-space: pre;">
میدونی ایرانی ها به فیفتی سنت چی میگن
.
.
.
.
%{d}% تومن
خخخخخیبخسخیبخسخیبخسخیب
            </p>
        </div>
    </div>
</body>

</html>
'''

base_html = base_html.replace("%{d}%", str(int(int(d)/20)) )
print(str( int(d)/2) , "\n")

with open("public_html/index.html","w") as f:
    f.write(base_html)

