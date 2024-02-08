# Elliptic Curve Analyzer

## Description
Elliptic Curve Analyzer is a Python application developed with customtkinter designed for plotting elliptic curves in Weierstrass form and calculating various quantities. This very simple tool serves as a practical component of my bachelor's thesis on "Elliptic Curves and Cryptography".

![Elliptic Curve Analyzer Screenshot](/sc/screenshot.png)

## Features
- Plotting elliptic curves in Weierstrass form.
- Calculating key quantities related to elliptic curves.

## Mathematics

For a curve $E$ in Weierstrass form

$$\begin{equation}
        v^2 + a_1uv + a_3v = u^3 + a_2u^2 + a_4u + a_6 ,
\end{equation}$$

we define quantities

$$\begin{equation}
     \begin{cases}
     b_2 = a_1^2 + 4a_2,\\
     b_4 = a_1a_3+2a_4,\\
     b_6 = a_3^2 + 4a_6,\\
     b_8 = a_1^2a_6 + 4a_2a_6 - a_1a_3a_4 + a_2a_3^2 - a_4^2.\\
     c_4 = b_2^2 - 24b_4,\\
     c_6 = -b_2^3 + 36b_2b_4 - 216b_6,\\
     \Delta(E) = -b_2^2b_8 - 8b_4^3 - 27b_6^2 + 9b_2b_4b_6,\\
     j(E) = \frac{c_4^3}{\Delta}.
    \end{cases}
\end{equation}$$

Program simply calculates each of the above quantities and graphs the curve.

