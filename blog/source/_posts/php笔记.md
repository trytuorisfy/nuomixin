title: php笔记
date: 2016-08-02 09:26:06
tags: 后端
---

其实我就是想简单的给我返回个json而已，直接上代码，[来源](http://zhidao.baidu.com/link?url=Fr8wfcc8-jytgV5VqsgSHEpKWFWnUnUREHRDPiOtB62ZlLGkllmaK7ZioUz2HN0xIib1hJ67eQcwY4dSfBu55SVSxmkiRhv6Ni4WNDzGXKu)

    <?php
    header('Content-type: text/json');
    $fruits = array (
        "success"  => true,
        "fruits"  => array("a" => "orange", "b" => "banana", "c" => "apple"),
        "numbers" => array(1, 2, 3, 4, 5, 6),
        "holes"   => array("first", 5 => "second", "third")
    );
    echo json_encode($fruits);
    ?>
