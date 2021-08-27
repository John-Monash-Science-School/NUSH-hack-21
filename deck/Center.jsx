import React from 'react';
import { Box } from 'theme-ui';

export default ({ children, width='100%' }) => (
  <Box
    style={{
      alignItems: 'center',
      justifyContent: 'center',
      display: 'flex',
      width: '100%',
      flexDirection: 'row'
    }}
  >
    <Box style={{width, textAlign: 'center'}}>
      {children}
    </Box>
  </Box>
)