(in-package :mrs)

(defun simple-io-mrsread (istream ostream)

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
      (setq imrs (read-mrs jstream))
      (setq robmrs (mrs-to-rmrs imrs))
      (output-rmrs1 robmrs 'mrs::xml ostream)
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)
