<?php
function han($w){
    $a[1]=1;
    $a[2]=1;
    for ($q=3;$q<=$w;$q++){
        $a[$q]=$a[$q-1]+$a[$q-2];
    }
    return $a;
}
