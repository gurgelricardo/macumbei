from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Ponto, Funcao, Linha 

def pagina_cadastro(request):
    contexto = {
        'funcoes': Funcao.choices,
        'linhas': Linha.choices
    }
    return render(request, 'pontos/cadastro.html', contexto)

@require_POST
def salvar_ponto(request):
    try:
        nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        linha = request.POST.get('linha')
        entidade = request.POST.get('entidade')
        letra = request.POST.get('letra')
        audio_file = request.FILES.get('audio_blob')

        if not all([nome, funcao, linha, letra, audio_file]):
            return JsonResponse({'status': 'erro', 'mensagem': 'Todos os campos e o áudio são obrigatórios.'}, status=400)
            
        novo_ponto = Ponto(
            nome=nome,
            funcao=funcao,
            linha=linha,
            entidade=entidade,
            letra=letra,
            link_audio=audio_file
        )
        novo_ponto.full_clean()
        novo_ponto.save()

        return JsonResponse({
            'status': 'sucesso',
            'mensagem': f'Ponto "{novo_ponto.nome}" salvo com sucesso!'
        }, status=201)

    except Exception as e:
        return JsonResponse({'status': 'erro', 'mensagem': str(e)}, status=500)
    
def listar_pontos(request):
    queryset = Ponto.objects.all().order_by('nome')

    nome_query = request.GET.get('nome')
    funcao_query = request.GET.get('funcao')
    linha_query = request.GET.get('linha')
    entidade_query = request.GET.get('entidade')
    letra_query = request.GET.get('letra')

    if nome_query:
        queryset = queryset.filter(nome__icontains=nome_query)
        
    if funcao_query:
        queryset = queryset.filter(funcao=funcao_query)
        
    if linha_query:
        queryset = queryset.filter(linha=linha_query)
        
    if entidade_query:
        queryset = queryset.filter(entidade__icontains=entidade_query)
        
    if letra_query:
        queryset = queryset.filter(letra__icontains=letra_query)

    contexto = {
        'pontos': queryset,
        'funcoes': Funcao.choices,
        'linhas': Linha.choices, 
        'search_values': request.GET
    }
    
    return render(request, 'pontos/listar.html', contexto)

def home_view(request):
    return render(request, 'pontos/home.html')
