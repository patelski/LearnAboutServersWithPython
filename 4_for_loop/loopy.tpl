<html>

    <head>
        <title>My page</title>
    </head>

    <body>
        <h2>Numbers and their squares</h2>
        %for item in items:
            <p>{{item}} : {{items.get(item)}}</p>
        %end
    </body>

</html>