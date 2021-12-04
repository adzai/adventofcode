#lang racket

(define lines (file->lines "aoc5-input.txt"))

(define (get-num line-chars ex1 ex2 cmp-char high low)
  (cond
    [(empty? line-chars) high]
    [(or (equal? (car line-chars) ex1)
         (equal? (car line-chars) ex2))
     (get-num (cdr line-chars) ex1 ex2 cmp-char high low)]
  [(equal? (car line-chars) cmp-char)
    (get-num (cdr line-chars) ex1 ex2 cmp-char
             (+ low (quotient (- high low) 2)) low)]
  [else
    (get-num (cdr line-chars)  ex1 ex2 cmp-char
             high (+ low (quotient (- high low) 2)))]))

(define (get-ids lines)
  (if (empty? lines)
    '()
    (begin
      (cons
      (+ (* (get-num (string->list (car lines)) #\R #\L #\F 127 0) 8)
         (get-num (string->list (car lines)) #\F #\B #\L 7 0))
      (get-ids (cdr lines))))))

(displayln (~a "Part 1: " (apply max (get-ids lines))))
(define x (sort (get-ids lines) <))
(define y (stream->list (in-range (car x) (last x))))
(define z (set-first (set-subtract (list->set y) (list->set x))))
(displayln (~a "Part 2: " z))
