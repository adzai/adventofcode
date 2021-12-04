#lang racket

(define lines (file->lines "aoc8-input.txt"))

(define vec
  (for/vector ([line lines]
               [i (in-naturals)])
    (vector-append (list->vector (string-split line)) (vector i))))

(define accumulator (box 0))

(define (jmp val line-num vec)
  (vector-ref vec (+ line-num (string->number val))))

(define (acc val line-num vec)
  (set-box! accumulator (+ (unbox accumulator)
                           (string->number val)))
  (vector-ref vec (add1 line-num)))

(define (nop val line-num vec)
  (vector-ref vec (add1 line-num)))

(define (match-commands vals vec)
  (match (vector-ref vals 0)
    ["jmp" (jmp (vector-ref vals 1)
                (vector-ref vals 2)
                vec)]
    ["acc" (acc (vector-ref vals 1)
                (vector-ref vals 2)
                vec)]
    ["nop" (nop (vector-ref vals 1)
                (vector-ref vals 2)
                vec)]))

(define (replace-jmp vec num)
  (define ctr (make-parameter 0))
  (for/vector ([v vec])
    (if (equal? (vector-ref v 0) "jmp")
      (if (= (ctr) num)
        (begin
          (ctr (add1 (ctr)))
          (vector "nop" (vector-ref v 1) (vector-ref v 2)))
        (begin
          (ctr (add1 (ctr)))
          v))
      v)))

(define (find-cycle vals processed vec)
  (if (= (vector-ref vals 2) (sub1 (vector-length vec)))
    "Terminated"
    (unless (member vals processed)
      (let ([res (match-commands vals vec)])
        (find-cycle res (cons vals processed) vec)))))

(define (find-terminating-sequence old-vec num)
  (set-box! accumulator 0)
  (define new-vec (replace-jmp old-vec num))
  (unless (equal? (find-cycle
                    (vector-ref new-vec 0) '() new-vec) "Terminated")
    (find-terminating-sequence old-vec (add1 num))))

(find-cycle (vector-ref vec 0) '() vec)
(displayln (~a "Part 1: " (unbox accumulator)))
(find-terminating-sequence vec 0)
(displayln (~a "Part 2: " (unbox accumulator)))
