#include "sys.h"
#include "delay.h"
#include "timer.h"
#include "led.h"
#include "dirc.h"
#include "usart.h"
#include "globalconfig.h"


u16 step_a[MotorNum] ={0, 0, 0, 0};
u16 step_d[MotorNum] = {10000, 20000, 10000, 20000};
u16 timcc[MotorNum]={500, 500, 500, 500};


int main(void)
{
	u8 i = 0;
	u8 dir[MotorNum] = {0, 1, 0, 1};
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	
	delay_init();
	LED_Init();

	uart_init(115200);
	
	DIR_GPIO_Configuration();
	Set_ALL_Dir_GPIO(dir);
	
	
	TIM_GPIO_Config_Init();
	
	TIM_NVIC_Configuration();
	
	TIM2_Congfig_Init(71);
	LED1_Flicker(2);

	while(1)
	{
		if(USART_RX_STA & 0x8000)
		{
			switch(USART_RX_BUF[0])
			{
				case 'a':
				{
					LED1_Flicker(3);
					for (i=0;i<MotorNum;i++)
						step_a[i] = 0;
					TIM2_Congfig_Init(71);
					TIM_Startup();
					break;
				}
				case 'c':
				{
					LED1_Flicker(2);
					for(i = 0; i<MotorNum; i++)
					{
						timcc[i] = str2u16(USART_RX_BUF, 1+2*i);
					}
					TIM_Shutdown();
					TIM2_Congfig_Init(71);
					break;
				}
				case 'd':
				{
					LED1_Flicker(2);
					for (i=1;i<MotorNum+1; i++)
					{
						dir[i-1] = USART_RX_BUF[i];
					}
					Set_ALL_Dir_GPIO(dir);
					break;
				}
//				case 's':
//				{
//					LED1_Flicker(2);
//					step_d = str2u16(USART_RX_BUF, 1);
//					break;
//				}
				default:
				{
					break;
				}
					
			}
			
			USART_RX_STA = 0;
		}
		
		
		delay_ms(100);
		LED0 = !LED0;
	}
}


