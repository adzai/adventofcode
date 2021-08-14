#lang racket/base

(require (only-in racket/list empty?)
         (only-in racket/file file->lines)
         (only-in racket/format ~a))

(struct runner
  (running? resting? speed orig-time current-time
            orig-rest-time current-rest-time traveled points)
  #:mutable #:transparent)

(define (runner-run-one-sec! runner)
  (set-runner-traveled! runner
                        (+ (runner-speed runner)
                           (runner-traveled runner)))
  (set-runner-current-time! runner (sub1 (runner-current-time runner)))
  (when
    (= (runner-current-time runner) 0)
    (set-runner-current-time! runner (runner-orig-time runner))
    (set-runner-running?! runner #f)
    (set-runner-resting?! runner #t)))

(define (runner-rest-one-sec! runner)
  (set-runner-current-rest-time! runner
                                 (sub1 (runner-current-rest-time runner)))
  (when
    (= (runner-current-rest-time runner) 0)
    (set-runner-current-rest-time! runner (runner-orig-rest-time runner))
    (set-runner-running?! runner #t)
    (set-runner-resting?! runner #f)))

(define (elapse-one-second runner)
  (if (runner-running? runner)
    (runner-run-one-sec! runner)
    (runner-rest-one-sec! runner))
  (runner-traveled runner))

(define (get-highest-runner-score get-proc runners [highest 0])
  (if (empty? runners)
    highest
    (let ([current (get-proc (car runners))])
      (if (> current highest)
        (get-highest-runner-score get-proc (cdr runners) current)
        (get-highest-runner-score get-proc (cdr runners) highest)))))

(define (day-14)
  (define input (file->lines "14.txt"))
  (define runners
    (for/list ([line input])
      (define-values (speed time rest-time)
        (apply values (map string->number (regexp-match* #px"[0-9]+" line))))
      (runner #t #f speed time time rest-time rest-time 0 0)))
  (for ([t (in-range 1 2503)])
    (define best-distance
      (apply max
             (for/list ([runner runners])
               (elapse-one-second runner))))
    (for ([runner runners])
      (when (= best-distance (runner-traveled runner))
        (set-runner-points! runner (add1 (runner-points runner))))))
  (displayln (~a "Part 1: " (get-highest-runner-score runner-traveled runners)))
  (displayln (~a "Part 2: " (get-highest-runner-score runner-points runners))))

(day-14)
