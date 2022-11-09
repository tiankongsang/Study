<table border="1">
    <?php for($a=1;$a<10;$a++) {?>
    <tr>
        <?php for ($s=1;$s<=$a;$s++){?>
        <td> <?php echo   $a . '*' . $s . '=' . $a * $s  ?> </td>
        <?php } ?>
    </tr>
    <?php }?>
</table>