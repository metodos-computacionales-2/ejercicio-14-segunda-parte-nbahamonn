Laboratorio 14

1. Solve the system for λ=1, What kind of equation you get?

   - Ecuacion diferencial lineal de segundo orden.

2. What kind of solutions are you expecting?

   - Se espera obtener como respuesta una funcion de seno o coseno.
  
3. Test your function of Euler to solve this equation and let it evolve for a given time (maybe 1000 computational times), print the value of t, y(0)n, y(1)n at every step and save a file with this information.

   - Codigo adjunto.

4. What do you see that it happens, how is the solution of the y(0)n as a function of time?

   - Se observa que la grafica es senosoidal y que su amplitud no varia con el paso del tiempo.
   
5. Now use the Runge-kutta solution and let it evolve the same quantity of time. export the data to a file and plot it. What can you conclude from both implementations.

   - Observando ambos metodos juntos se puede concluir que el metodo de Euler tiene algunas variaciones en la elipse que se forma, no da una elipse simetrica, mientras que con el metodo de rk4 la elipse es simetrica, siendo este el metodo mas acertado.

6. Now plot the solution of y(0)n vs y(1)n, what do you expect to see? what do you see and what does it mean?

   - Al plotear y(0)n vs y(1)n, se obtiene una elipse. Debido a que las ondas generadas por y(0)n y y(1)n, son senosoidales y cosenosoidales.

7. Now include a term of friction in the Differential equation.

                       ffric=−γv
                       
   - Al añadir la friccion hace que la funcion que antes era senosoidal infinita comience a disminuir su amplitud, hasta que esta llegue a 0.
                       
                       
8. Test with different values of λ (just with Rungekutta), what can you say about the power used in λ

   - Si se aumenta lambda deja funcionar debido a que la ecuacion ya no seria lineal. 
