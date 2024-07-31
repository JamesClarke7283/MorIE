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