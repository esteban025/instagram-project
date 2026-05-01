from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from instagram.forms import PostForm

# Create your views here.
@login_required
def create_post(request, user_id):
    # Print 1: Verificar si entramos a la función y qué ID llega por URL
    print(f"--- DEBUG: Entrando a la vista para user_id: {user_id} ---")
    print(f"--- DEBUG: Usuario en sesión: {request.user.id} ({request.user.username}) ---")

    if request.user.id != user_id:
        print("--- DEBUG: Bloqueado por seguridad: IDs no coinciden ---")
        return redirect('home')

    if request.method == 'POST':
        # Print 2: Confirmar que el formulario se envió por POST
        print("--- DEBUG: Petición POST recibida ---")
        
        form = PostForm(request.POST, request.FILES)
        
        # Print 3: Ver qué datos crudos llegaron en el diccionario POST y FILES
        print(f"--- DEBUG: Data recibida: {request.POST} ---")
        print(f"--- DEBUG: Archivos recibidos: {request.FILES} ---")

        if form.is_valid():
            print("--- DEBUG: El formulario es VÁLIDO ---")
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print(f"--- DEBUG: Post guardado con éxito. ID: {post.id} ---")
            return redirect('profile_detail', pk=user_id)
        else:
            # Print 4: Si no es válido, imprimir exactamente por qué
            print("--- DEBUG: El formulario es INVÁLIDO ---")
            print(f"--- DEBUG: Errores del formulario: {form.errors.as_json()} ---")
    else:
        print("--- DEBUG: Petición GET - Cargando formulario vacío ---")
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
