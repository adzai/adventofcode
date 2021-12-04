#lang racket

(define lines (map string->number (file->lines "aoc9-input.txt")))

(define (find-corrupted lines)
  (define-values (preamble rst) (split-at lines 25))
  (let* ([num-to-check (car rst)]
         [comb-lst (sequence->list (in-combinations preamble 2))]
         [sum-lst (map (λ (lst) (apply + lst)) comb-lst)]
         [corrupted? (not (member num-to-check sum-lst))])
    (if corrupted? num-to-check (find-corrupted (cdr lines)))))

(define (find-contiguous-set lines num-to-check [nums '()])
  (if (<= (apply + nums) num-to-check)
    (let* ([new-lst (append nums (list (car lines)))]
           [sum (apply + new-lst)])
      (cond
        [(= sum num-to-check)
         (+ (apply min new-lst) (apply max new-lst))]
        [(< sum num-to-check)
         (find-contiguous-set (cdr lines) num-to-check new-lst)]
        [else
          (find-contiguous-set (cdr lines) num-to-check (cdr new-lst))]))
    (find-contiguous-set lines num-to-check (cdr nums))))

(define corrupted-num (find-corrupted lines))
(displayln (~a "Part 1: " corrupted-num))
(displayln (~a "Part 2: "(find-contiguous-set lines corrupted-num)))
