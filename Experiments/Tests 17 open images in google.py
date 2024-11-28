import webbrowser as web

name = input("Name: ")

name = name.replace(" ", "+")
values = f"https://www.google.com/search?sca_esv=eeb7227c5a3e2591&sca_upv=1&rlz=1C1CHZL_enIN869IN870&sxsrf=ACQVn0-816oCuNopJhxpcqfhKiADzi-f4w:1712736280834&q={name}&uds=AMwkrPuUJbKUxs7JuHyJaz8jErk2XsPyBR_FgEI4e7QLJHvTntX-YaFMJm6Q-gN6C7Xc6ayoBmbn0QV2nhI4Wcd1WlHSGRMNL_Q6mzWLTS07KFkC_PkKepT4mkpehwWbdskF3GhdaMCRTcRtH8DDRyNwEiDtMGHxBfTGD8OACw0efoWqnC7hdg-my9kBLBmzDHRbTrGN62HlOT2_0WFPBh7fzpVc7xjJ7PfgvNLXq2HWWXndz11eFcdbIF-Fdc2B4XRzY3Rxi37o6GsSvpz441NkM6iYsqJGHNfOWrMCB6hL_BwmS2KwvGk&udm=2&prmd=isvnmbtz&sa=X&ved=2ahUKEwjlsfPsl7eFAxUj-zgGHelsDEMQtKgLegQIDRAB&biw=1536&bih=730&dpr=1.25"
web.open_new(values)

"""This program can successfuly open the images of the provided input"""
