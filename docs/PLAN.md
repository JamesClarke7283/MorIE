# PLAN for making MorIE.

We need to use customtkinter and CTkMessagebox to make a simple to use GUI in python for the MorIE equasion layed out in our paper.

Use sliders for morality values.

Put the equasion logic in the src.core.morie module, all ui components go in the src.components.[xy] modules.

The output needs to be a value (floating point number), A word that says "NET POSITIVE" or "NET NEGATIVE". It should say "from -10 to 10 where on the scale should a moral value quantify as the bare minimum for good".


## Structure
$ tree . --gitignore
.
├── docs
│   └── PLAN.md
├── LICENSE
├── pyproject.toml
├── README.md
└── src
    ├── app.py
    ├── components
    └── core

# Test walkthroughs

1. Positive Scenario

5 - 0 = 5
n1 - B1 =C

1 x 5 = 5
Dg x C = Dg(F)

4 - 1 = 3
n2 - B2 =C2

0.5 x 3 = 1.5
Ig x C2 = Ig(F)


1 x -0.5 = -0.5
B2 x IB = IB(F)


-1 x 0 = 0
Db x b1 = Db(F)

5 + 1.5 = 6.5
Dg(f) + Ig(f) = total good

0 + -0.5 = -0.5
Db(f) + Ib(f) = total bad

total intent = I
I= 1

total intent + Total good + total bad = net outcome
1 + 6.5 - 0.5 = 7



