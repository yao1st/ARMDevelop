#include "sys.h"
#include "delay.h"
#include "timer.h"
#include "led.h"
#include "usart.h"
u32 cnt;
u16 cnt1;
u16 step1d;
u16 step1a;
int main(void)
{
	u16 arr = 3;
	u16 psc = 17;
//	u16 xifen = 10000;
	cnt = 0;
	cnt1 = 250;
	step1d = 40000;
	step1a = 0;
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	delay_init();
	LED_Init();
	uart_init(115200);
//	delay_ms(3000);
	TIM2_Int_Init(arr, psc);
	while(1)
	{
		LED1 = !LED1;
		delay_ms(1000);
	}
}

