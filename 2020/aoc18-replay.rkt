#lang racket


(define lines (file->lines "aoc18-input.txt"))

(define (process-calculation x operand y)
  (if (equal? operand "+")
    (~a (+ (string->number x) (string->number y)))
    (~a (* (string->number x) (string->number y)))))

(define (consume-single curried-func tokens #:in-paren in-paren)
  (when (and in-paren (not (procedure? curried-func))
             (not (or (empty? tokens) (equal? (car tokens) ")"))))
    (set! curried-func (curry process-calculation curried-func)))
  (if (or (and (not (procedure? curried-func))
           (not in-paren))
          (empty? tokens))
    (values curried-func tokens)
    (cond
      [(equal? (car tokens) "(")
     (let-values ([(x y) (consume-single process-calculation (cdr tokens) #:in-paren #t)])
    (consume-single (curry curried-func x)
                    y
                    #:in-paren #t))]
      [(equal? (car tokens) ")")
       (consume-single curried-func (cdr tokens) #:in-paren #f)]
    [else (consume-single (curry curried-func (car tokens))
                    (cdr tokens)
                    #:in-paren in-paren)])))

(define (evaluate tokens [collected '()])
  (cond
    [(empty? tokens) collected]
    [(equal? (car tokens) ")")
     (evaluate (cdr tokens) collected)]
    [else
     (let-values ([(x y) (consume-single process-calculation (if (equal? (car tokens) "(") (append (if (empty? collected) collected (list collected)) (cdr tokens)) (append (if (empty? collected) collected (list collected)) tokens)) #:in-paren #f)])
       (if (empty? y) x
         (evaluate y x)))]))

(define (get-tokens str)
  (map ~a (string->list (string-replace str " " ""))))

(define res (for/sum ([line lines])
              (string->number (evaluate (get-tokens line)))))

(displayln res)
