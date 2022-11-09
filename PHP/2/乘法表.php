<!doctype html>

<head>
    <title>PHP应用9x9</title>
    <style>
        tr,td {
            border: 2px solid #78626c;
        }
    </style>
</head>

<body>
    <?php
    echo "九九乘法表";
    for ($i = 1; $i <= 9; $i++) {
        echo "<table border='1'><tr>";
        for ($j = 1; $j <= $i; $j++) {
            echo "<td width='60' align='center'>";
            echo "$j*$i=" . $j * $i;
            echo "</td>";
        }
    }
    echo "</tr></table>";
    ?>
</body>

</html>