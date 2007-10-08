(in-package :common-lisp-user)

(defun simple-io-read-block (istrm &key (term-char 23))

  (defvar *indata* (make-array 512 :initial-element 0 :element-type '(unsigned-byte 8)))
  (defvar *outdata* (make-array 4 :initial-element 0 :element-type '(unsigned-byte 8)))

  (setq ostrm (make-string-output-stream))

  (loop

    (setq len (read-sequence *indata* istrm))
    (if (< len 512)
      (return-from simple-io-read-block nil))

    (setq i 0)
    (setq o 0)
    (loop
      (if (>= i len) (return))
      (setq inp (aref *indata* i))
      (setq i (+ i 1))
      (if (= inp term-char)
        (return-from simple-io-read-block (get-output-stream-string ostrm)))
      (when (or (>= inp 32) (member inp '(9 10 13)))
        (setf (aref *outdata* o) inp)
        (setq o (+ o 1))
        (setq strng (excl::octets-to-string *outdata* :external-format :utf-8 :truncate t :end o))
        (when (string/= strng "")
          (setq o 0)
          (write-string strng ostrm)
        )
      )
    )

  )
)

(defun simple-io-write-delim (ostream)
  (format ostream "~a" (code-char 23))
  (dotimes (i 511)
    (format ostream "~a" (code-char 0))
  )
)



(in-package :mrs)

(defvar *rasp-rmrs-gram-file*)
(defvar *rasp-rmrs-tag-file*)
(defvar *rasp-xml-word-p*)
(defvar *rasp-xml-type*)

(defun simple-io-rasp-rmrs (istream ostream)

  (let ((*rasp-rmrs-gram-file*
         "src/rmrs/rasp3/gram15.rmrs")
        (*rasp-rmrs-tag-file*
         "src/rmrs/rasp3/lex15.rmrs")
        (*rasp-xml-word-p* t)
        (*renumber-hack* t)
        (*rasp-xml-type* :none))

    (setf *algebra-rule-instructions* nil)
    (setf *algebra-tag-instructions* nil)

    (clear-rule-record)
    (read-rmrs-grammar *rasp-rmrs-gram-file*)
    (read-rmrs-tag-templates *rasp-rmrs-tag-file*)

    (setf (stream-external-format istream) :utf-8)
    (setf (stream-external-format ostream) :utf-8)

    (common-lisp-user::simple-io-write-delim ostream)
    (finish-output ostream)

    (loop

      (setq input (common-lisp-user::simple-io-read-block istream))

      (if (not input)
        (return))

      (with-input-from-string (jstream input)
        (setf (stream-external-format jstream) :utf-8)
        (format ostream "<rmrs-list>~%")
        (setq tagged (read jstream nil nil))
        (setq number (read jstream nil nil))
        (loop
          (setq tree (read jstream nil nil))
          (unless tree
            (return))
          (when tree
            (construct-sem-for-tree 
              tree
              :rasp ostream tagged))
        )
        (format ostream "</rmrs-list>~%")
        (common-lisp-user::simple-io-write-delim ostream)
        (finish-output ostream)
      )

    )

  )

)



(in-package :preprocessor)

(defun simple-io-preprocess (istream ostream)

  (setf (stream-external-format istream) :utf-8)
  (setf (stream-external-format ostream) :utf-8)

  (read-preprocessor "preprocessor.fsr") 

  (common-lisp-user::simple-io-write-delim ostream)
  (finish-output ostream)

  (loop

    (setq input (common-lisp-user::simple-io-read-block istream))

    (if (not input)
      (return))

    (with-input-from-string (jstream input)
      (setf (stream-external-format jstream) :utf-8)
      (format ostream "~a~%" (preprocessor:preprocess input :format :smaf))
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)
