SC_DUR = "(\\\dur(.+?)\n)"
SC_BD_DUR = "(~bd =)(.|\n)*?(\\\dur(.+?)\n)"
SC_SN_DUR = "(~sn =)(.|\n)*?(\\\dur(.+?)\n)"
SC_CH_DUR = "(~ch =)(.|\n)*?(\\\dur(.+?)\n)"
SC_RD_DUR = "(~rd =)(.|\n)*?(\\\dur(.+?)\n)"
SC_SY_DUR = "(~synth =)(.|\n)*?(\\\dur(.+?)\n)"
SC_SY_DEG = "(~synth =)(.|\n)*?(\\\degree(.+?)\n)"

SC_BD_RHYTHMS = {
"\\dur, Pseq([4],inf),\n": ["\\dur, Pseq([2,2],inf),","\\dur, Pbjorklund2(3,8,inf),"],
"\\dur, Pbjorklund2(3,8,inf),\n": ["\\dur, Pbjorklund2(3,8,inf)/2,", "\\dur, Pseq([4],inf),"],
"\\dur, Pseq([2,2],inf),\n": ["\\dur, Pseq([4],inf),","\\dur, Pbjorklund2(3,8,inf),"],
"\\dur, Pbjorklund2(3,8,inf)/2,\n": ["\\dur, Pbjorklund2(3,8,inf),", "\\dur, Pseq([4],inf),"],
}

SC_SN_RHYTHMS = {
"\\dur, Pseq([4],inf),\n": ["\\dur, Pseq([Rest(2),2],inf),","\\dur, Pbjorklund2(3,16,inf),"],
"\\dur, Pbjorklund2(3,16,inf),\n": ["\\dur, Pseq([Rest(2),2],inf),","\\dur, Pseq([Rest(2),2],inf),"],
"\\dur, Pseq([Rest(2),2],inf),\n": ["\\dur, Pbjorklund2(3,16,inf),","\\dur, Pbjorklund2(3,16,inf),"],
}

SC_CH_RHYTHMS = {
"\\dur, Pseq([4],inf),\n": ["\\dur, Pseq([1],inf),","\\dur, Pbjorklund2(3,16,inf)/2,"],
"\\dur, Pbjorklund2(3,16,inf)/2,\n": ["\\dur, Pseq([1],inf),","\\dur, Pseq([1],inf),"],
"\\dur, Pseq([1],inf),\n": ["\\dur, Pbjorklund2(3,16,inf)/2,","\\dur, Pbjorklund2(3,16,inf)/2,"],
}

SC_RD_RHYTHMS = {
"\\dur, Pseq([4],inf),\n": ["\\dur, Pseq([2],inf),","\\dur, Pbjorklund2(3,7,inf),"],
"\\dur, Pbjorklund2(3,7,inf),\n": ["\\dur, Pseq([2],inf),","\\dur, Pseq([2],inf),"],
"\\dur, Pseq([2],inf),\n": ["\\dur, Pbjorklund2(3,7,inf),","\\dur, Pbjorklund2(3,7,inf),"],
}

SC_SY_DEGREE = {
"\\degree, Pseq([[0,2,4]],inf),\n": ["\\degree, Pseq([1],inf),","\\degree, Pseq([[3,5,7]],inf),"],
"\\degree, Pseq([1],inf),\n": ["\\degree, Pseq([[0,2,4]],inf),","\\degree, Pseq([[3,5,7]],inf),"],
"\\degree, Pseq([[3,5,7]],inf),\n": ["\\degree, Pseq([1],inf),","\\degree, Pseq([[0,2,4]],inf),"]
}
