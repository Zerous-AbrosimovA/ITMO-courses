# Пользовательские типы данных

`enum` - перечисление\
`enum inentifier {enumerated-list}` // до С23\
`enum inentifier -> type {enumerated-list}` // С23
``` C
enum color {RED, GREEN, BLUE}
enum color c = RED
```
`typedef enum color color_t` - сокращение обращения к enum\
В C есть switch-case (**удивительно**) и пишется он эквивалентно java
## Устройство Даффа
``` C
int num = 11;
int count = (n + 3); / 4;
int i = 0;
switc (num % 4) 
{
	case 0:
	do
	{
		++i;
		case 3: ++i;
		case 2: ++i;
		case 1: ++i;
	} while (--count > 0);
}
```
# Структуры

``` C
typedef struct Point1 // в структуре нельзя создавать функции, только поля
{
	double x;
	double y;
	double z;
} Point;
```
В структуре sizeof вернет **выравненное значение**, то есть, если есть 3 поля double и 1 поле int, то размер структуры будет равен 4 * 8 = 32, т.к int будет выравнен до double\
`typedef enum color {RED...} color_t`\
`#pragma pack(push, 1)` - плотная упаковка без выравнивания (обращение долгое)
``` C
typedef struct Point
{
	char x, y;
	int z;
	color_t color;
	short w;
} Point 5;
#pragma pack(pop)
```
`offsetof(Point5, x)` - узнать смещение поля, но нужно заимпортить stddef.f\
`unuin` - структура, в которой у каждого поля offset 0;
``` C
struct S {
	unsigned b1 : 5; // отводим под unsigned 5 бит
	unsigned : 11; // дырка в 11 бит
	unsigned b2 : 6;
} // это не надо юзать
```
# Выделение памяти для массива массивов 

``` C
int **b = malloc(H*sizeof(int *));
for (int i = 0; i < H; i++) {
	malloc(W * sizeof(int));
}
```
