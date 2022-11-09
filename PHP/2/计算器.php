<?php
if (empty($_POST)) {
    $a = array('num1' => 0, 'num2' => 0, 'fuhao' => '');
} else {
    $a = $_POST;
}
$sum = '';
if ($a['num1'] != '' && is_numeric($a['num1']) && $a['num2'] != '' && is_numeric($a['num2'])) {
    $fuhao = $a['fuhao'];
    switch ($fuhao) {
        case '+':
            $sum =  $a['num1'] + $a['num2'];
            break;
        case '-':
            $sum =  $a['num1'] - $a['num2'];
            break;
        case '*':
            $sum =  $a['num1'] * $a['num2'];
            break;
        case '/':
            $sum = $a['num1'] / $a['num2'];
            break;
        case '%':
            $sum =  $a['num1'] % $a['num2'];
            break;
    }
}
?>

<head>
    <title>计算器</title>
    <style>
        .head {
            background-color: red;
            height: 50px;
            line-height: 50px;
            padding-left: 200px;
            font-size: 25px;
        }

        .box {
            height: 80px;
            width: 490px;
            margin: auto;
            position: relative;
            border: 1px solid red;
            border-color: red;

        }
    </style>
</head>

<body>
    <div class="box">
        <div class="head">计算器</div>
        <form action="" method="POST">
            <input type="number" name="num1">
            <select name="fuhao" id="" 1>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
                <option value="%">%</option>
            </select>
            <input type="number" name="num2">

            <input type="submit" name="=" value="=">
            <input type="text" value="<?php echo $sum; ?>" size="1">
        </form>
    </div>

</body>

</html>