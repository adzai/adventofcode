#lang racket/base

(require racket/file
         racket/string)

(define vec (file->lines "aoc2-input.txt"))

(define (xor x y) (not (equal? x y)))

; Part 1
(displayln (for/sum ([elem vec])
             (let* ([x (string-split elem)]
                    [num-sp (string-split (car x) "-")]
                    [n1 (string->number (car num-sp))]
                    [n2 (string->number (cadr num-sp))]
                    [char (string-ref (cadr x) 0)]
                    [pw (string->list (caddr x))]
                    [cnt (foldr (λ (x y)
                                   (if (equal? x char)
                                     (add1 y)
                                     y)) 0
                                pw)])
               (if (and (>= cnt n1) (<= cnt n2))
                 1 0))))

; Part 2
(displayln (for/sum ([elem vec])
             (let* ([x (string-split elem)]
                    [num-sp (string-split (car x) "-")]
                    [n1 (string->number (car num-sp))]
                    [n2 (string->number (cadr num-sp))]
                    [char (string-ref (cadr x) 0)]
                    [pw (list->vector (string->list (caddr x)))])
               (if (xor (equal? char (vector-ref pw (sub1 n1)))
                        (equal? char (vector-ref pw (sub1 n2))))
                 1 0))))
