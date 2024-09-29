/* primary_header.h */
#ifndef _PRIMARY_HEADER_H
#define _PRIMARY_HEADER_H

#include <stdio.h>

/* Forward declare the primary workhorse function */
void primary();

/* Also define a helper function */
void helper()
{
    printf("I'm a helper function and I helped!\n");
}
#endif /* _PRIMARY_HEADER_H */
