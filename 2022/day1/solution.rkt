#lang racket

(define input (file->lines "input.txt"))

(define total-calories
  (let loop ([input input]
             [current-elfs-calories '()]
             [total-calories '()])
    (cond
      [(empty? input)
       (sort (cons (apply + current-elfs-calories) total-calories) >)]
      [(string=? (car input) "")
       (loop (cdr input) '() (cons (apply + current-elfs-calories)
                                   total-calories))]
      [else (loop (cdr input) (cons (string->number (car input))
                                    current-elfs-calories)
                  total-calories)])))

(displayln (~a "Part 1: " (car total-calories)))
(displayln (~a "Part 2: " (apply + (take total-calories 3))))
