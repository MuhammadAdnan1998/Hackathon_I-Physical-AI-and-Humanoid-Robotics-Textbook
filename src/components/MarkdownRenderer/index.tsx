import React from 'react';
import ReactMD from '../ReactMD';

interface MarkdownRendererProps {
  children: string;
}

const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ children }) => {
  return (
    <ReactMD>
      {children}
    </ReactMD>
  );
};

export default MarkdownRenderer;