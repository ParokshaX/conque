so test.vim

" test terminal

let sub = conque_term#new_terminal('bash')
let output = sub.read(2000)
call AssertEquals('nraffo@nraffo-laptop:~/.vim/tests$ ', output)
call sub.close()

" test subprocess

let sub = conque_term#new_subprocess('whoami')
let output = sub.read(500)
call AssertEquals('nraffo', output)
call sub.close()

" test callback

function! MyCB(output)
    echo a:output
endfunction

let sub = conque_term#new_subprocess('bash')
call sub.set_callback('MyCB')
call sub.write('pwd')
