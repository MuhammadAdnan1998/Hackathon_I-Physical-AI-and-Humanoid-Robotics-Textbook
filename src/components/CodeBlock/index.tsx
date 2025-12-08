import React, { FC, memo } from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/cjs/styles/prism';

interface CodeBlockProps {
  language: string;
  children: React.ReactNode;
}

const CodeBlock: FC<CodeBlockProps> = ({ language, children }) => {
  return (
    <SyntaxHighlighter language={language} style={oneDark} PreTag="div">
      {String(children)}
    </SyntaxHighlighter>
  );
};

export default memo(CodeBlock);
