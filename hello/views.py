from django.http import HttpResponse

def home(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @keyframes animatezoom {
        from {transform: scale(0)} 
        to {transform: scale(1)}
    }
    #id1{
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0,0,0);
        background-color: rgba(0,0,0,0.4);
        padding-top: 60px;
    }
    .container{
        background-color: #fefefe;
        margin: 5% auto 15% auto;
        border: 1px solid #888;
        border-radius: 10%;
        width: 70%;
        text-align: center;
        animation: animatezoom 1s;
    }
    input{
        width: 50%;
    }
    .header{
        position: relative;
        width: 100%;
    }
    .close{
        position: absolute;
        right: 2%;
        font-weight: bold;
        font-size: 35px;
        color: red;
        cursor: pointer;
    }
    .TIM{
        text-align: center;
        color: red;
        text-decoration: underline;
    }
    body{
        text-align: center;
    }
    @media screen and (min-width: 600px){
        .container{
            width: 50%;
        } 
    }
    @media screen and (min-width: 1200px){
        .container{
            width: 30%;
        } 
    }
    </style>
    <title>login</title>
</head>
<body>
    <h1 class="TIM">Hallo Tim!!!</h1>
    <button class="loginb" onclick="document.getElementById('id1').style.display='block'">Log In</button>

    <div id="id1">

        <div class="container">
            <div class="header">
                <span class="close" onclick="document.getElementById('id1').style.display='none'">&times;</span>
                <br>
                <h2>Log In</h2>
            </div>
            <input type="text" placeholder="Username">
            <br><br>
            <input type="text" placeholder="Password">
            <br><br>
            <button class="loginb">log in</button>
            <br><br>
        </div>

    </div>

    <script>
    var modal = document.getElementById('id1');

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    </script>
</body>
</html>""")