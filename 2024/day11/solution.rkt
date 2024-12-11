#lang racket

(require memo)


(define stones (string-split (car (file->lines "input.txt")) " "))
(define cache (make-hash))

(define/memoize (process-stone stone idx target)
  (define len (string-length stone))
  (define cache-hit (hash-ref cache stone #f))
  (cond 
    [(= idx target) 1]
    [cache-hit 
      (if (list? cache-hit) 
        (+ (process-stone (car cache-hit) (add1 idx) target) 
           (process-stone (cadr cache-hit) (add1 idx) target))
        (process-stone cache-hit (add1 idx) target))]
    [(string=? stone "0") (process-stone "1" (add1 idx) target)]
    [(= (modulo len 2) 0)
     (define stone-left (number->string (string->number (substring stone 0 (quotient len 2)))))
     (define stone-right (number->string (string->number (substring stone (quotient len 2) len))))
     (hash-set! cache stone (list stone-left stone-right))
     (+ (process-stone stone-left (add1 idx) target) 
        (process-stone stone-right (add1 idx) target))]
    [else 
      (define new-stone (number->string (* (string->number stone) 2024)))
      (hash-set! cache stone new-stone)
      (process-stone new-stone (add1 idx) target)]))


(displayln (~a "Part 1: " (for/sum ([stone stones]) (process-stone stone 0 25))))
(displayln (~a "Part 2: " (for/sum ([stone stones]) (process-stone stone 0 75))))
