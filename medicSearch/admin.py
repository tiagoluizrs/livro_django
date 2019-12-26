from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'created_at'

    # Preenche os campos varios na vizualização da lista
    empty_value_display = '-vazio-'

    # Lista de campos que serão exibidos no formulário de criação e edição
    # fields = ('user', ('role', 'status'), 'birthday' , 'specialties', 'addresses',)

    # Lista de campos que não serão exibidos no formulário de criação e edição
    exclude = ('created_at', 'updated_at',)

    # Lista de campos que serão exibidos na listagem da tela de listagem do admin
    list_display = ('user', 'status', 'role', 'birth', 'specialtiesList', 'addressesList',)

    # Itens que serão clicáveis na listagem da tela.
    list_display_links = ('user', 'status', 'birth')

    # Lista de campos que poderão ser filtrados na tela de listagem do admin. As foreinkeys precisam do __ e do nome do campo.
    list_filter = ('status',)

    # Deixa o campo apenas como leitura. Faremos isso aqui para que não seja permitido alterar o usuário atrelado a este perfil.
    readonly_fields = ('user',)

    # Lista de campos que poderão ser pesquisados na tela de listagem do admin. As foreinkeys precisam do __ e do nome do campo.
    search_fields = ('user__username',)

    # Similar ao field, porem aqui podemos agrupar os campos no formulário para que ele fique dividido de forma organizada na tela.
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Estado e função', {
            'fields': ('status', 'role')
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )

    # Métodos que foram criados para retornarmos em lista os campos que são ManyToMany para que sejam exibidos na listagem da tela do admin.
    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

    # Método que criamos para poder manipular os dados de um campo. No caso usamos para podermos manipular o campo vário do birthday. Qualquer outro campo poderia ser manipulado, apenas criando um método para ele e colocando o nome do método na listagem do list_display e do fields.
    def birth(self, obj):
        return obj.birthday
    birth.empty_value_display = '___/___/_____'

    # Adicionando arquivos no admin
    class Media:
        css = {
            "all": ("my_styles.css",)
        }
        js = ("my_code.js",)



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
