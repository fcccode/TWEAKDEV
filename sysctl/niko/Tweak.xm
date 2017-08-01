#include <sys/sysctl.h>
#include <sys/types.h>
#import <substrate.h>


int (*old_sysctl)(int *a , u_int mib,struct kinfo_proc *info , size_t size , void *e , size_t f) ; 


int sysctlHook(int *a , u_int mib , struct kinfo_proc  *info ,size_t size , void *e , size_t f ){

	printf("dddddd\n") ; 
	int value = old_sysctl(a,mib ,info ,size , e , f) ; 
	info->kp_proc.p_flag = 0 ; 
	return value ; 
}

%ctor {
	
	MSHookFunction((int *)sysctl ,(void *)sysctlHook, (void **)&old_sysctl  ) ; 
}






