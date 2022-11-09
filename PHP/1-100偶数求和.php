<?php
$sum=0;
for ($a=1;$a<=100;$a++){
    if($a%2==0){
        $sum=$sum+$a;
    }
}
echo $sum;