#lang racket

(define input (file->lines "2.txt"))

#;(define input
  '(
    "forward 5"
    "down 5"
    "forward 8"
    "up 3"
    "down 8"
    "forward 2"))

(define (match-part1 cmd num horizontal depth)
  (match cmd
    ["forward" (values (+ horizontal num) depth)]
    ["down" (values horizontal (+ depth num))]
    ["up" (values horizontal (- depth num))]))

(define (match-part2 cmd num horizontal depth aim)
  (match cmd
    ["forward" (values (+ horizontal num) (+ depth (* aim num)) aim)]
    ["down" (values horizontal depth (+ aim num))]
    ["up" (values horizontal depth (- aim num))]))

(define (move input [horizontal 0] [depth 0] [aim 0] #:part2? [part2? #f])
  (cond
    [(empty? input)
     (* horizontal depth)]
    [else (define str-lst (string-split (car input) " "))
          (define cmd (car str-lst))
          (define num (string->number (cadr str-lst)))
          (if part2?
            (let-values ([(new-horizontal new-depth aim) (match-part2 cmd num horizontal depth aim)])
              (move (cdr input)
                    new-horizontal
                    new-depth
                    aim
                    #:part2? #t))
            (let-values ([(new-horizontal new-depth) (match-part1 cmd num horizontal depth)])
              (move (cdr input)
                    new-horizontal
                    new-depth)))]))

(displayln (format "Part 1: ~a" (move input)))
(displayln (format "Part 2: ~a" (move input #:part2? #t)))
