<html>

    <head>
        <title>My page</title>
    </head>

    <body>
        <p>The dictionary: {{ stuff }}</p>
        <p>My name: {{ stuff.get('me') }}</p>
        <p>My city: {{ stuff.get('city') }}</p>
    </body>

</html>