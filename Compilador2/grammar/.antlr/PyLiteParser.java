// Generated from d:/Automatas_Practicas/Proyecto/Compilador2/grammar/PyLiteParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PyLiteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INDENT=1, DEDENT=2, FALSE=3, AWAIT=4, ELSE=5, IMPORT=6, PASS=7, NONE=8, 
		BREAK=9, EXCEPT=10, IN=11, RAISE=12, TRUE=13, CLASS=14, FINALLY=15, IS=16, 
		RETURN=17, AND=18, CONTINUE=19, FOR=20, LAMBDA=21, TRY=22, AS=23, DEF=24, 
		FROM=25, NONLOCAL=26, WHILE=27, ASSERT=28, DEL=29, GLOBAL=30, NOT=31, 
		WITH=32, ASYNC=33, ELIF=34, IF=35, OR=36, YIELD=37, PLUS=38, MINUS=39, 
		STAR=40, DOUBLESTAR=41, SLASH=42, DOUBLESLASH=43, PERCENT=44, EQ=45, NEQ=46, 
		LE=47, GE=48, LT=49, GT=50, ASSIGN=51, PLUS_ASSIGN=52, MINUS_ASSIGN=53, 
		STAR_ASSIGN=54, SLASH_ASSIGN=55, DSLASH_ASSIGN=56, PERCENT_ASSIGN=57, 
		POWER_ASSIGN=58, AMP_ASSIGN=59, PIPE_ASSIGN=60, CARET_ASSIGN=61, RSHIFT_ASSIGN=62, 
		LSHIFT_ASSIGN=63, WALRUS=64, AMP=65, PIPE=66, CARET=67, TILDE=68, LSHIFT=69, 
		RSHIFT=70, LPAREN=71, RPAREN=72, LBRACKET=73, RBRACKET=74, LBRACE=75, 
		RBRACE=76, COMMA=77, COLON=78, DOT=79, SEMI=80, AT=81, ARROW=82, ELLIPSIS=83, 
		NAME=84, INT=85, FLOAT=86, STRING=87, COMMENT=88, WS=89, NEWLINE=90;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_simpleStmt = 2, RULE_smallStmt = 3, 
		RULE_assignStmt = 4, RULE_assignOp = 5, RULE_exprStmt = 6, RULE_returnStmt = 7, 
		RULE_compoundStmt = 8, RULE_ifStmt = 9, RULE_whileStmt = 10, RULE_forStmt = 11, 
		RULE_funcDef = 12, RULE_paramList = 13, RULE_block = 14, RULE_expr = 15, 
		RULE_argList = 16, RULE_atom = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "simpleStmt", "smallStmt", "assignStmt", "assignOp", 
			"exprStmt", "returnStmt", "compoundStmt", "ifStmt", "whileStmt", "forStmt", 
			"funcDef", "paramList", "block", "expr", "argList", "atom"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'False'", "'await'", "'else'", "'import'", "'pass'", 
			"'None'", "'break'", "'except'", "'in'", "'raise'", "'True'", "'class'", 
			"'finally'", "'is'", "'return'", "'and'", "'continue'", "'for'", "'lambda'", 
			"'try'", "'as'", "'def'", "'from'", "'nonlocal'", "'while'", "'assert'", 
			"'del'", "'global'", "'not'", "'with'", "'async'", "'elif'", "'if'", 
			"'or'", "'yield'", "'+'", "'-'", "'*'", "'**'", "'/'", "'//'", "'%'", 
			"'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "'='", "'+='", "'-='", 
			"'*='", "'/='", "'//='", "'%='", "'**='", "'&='", "'|='", "'^='", "'>>='", 
			"'<<='", "':='", "'&'", "'|'", "'^'", "'~'", "'<<'", "'>>'", "'('", "')'", 
			"'['", "']'", "'{'", "'}'", "','", "':'", "'.'", "';'", "'@'", "'->'", 
			"'...'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INDENT", "DEDENT", "FALSE", "AWAIT", "ELSE", "IMPORT", "PASS", 
			"NONE", "BREAK", "EXCEPT", "IN", "RAISE", "TRUE", "CLASS", "FINALLY", 
			"IS", "RETURN", "AND", "CONTINUE", "FOR", "LAMBDA", "TRY", "AS", "DEF", 
			"FROM", "NONLOCAL", "WHILE", "ASSERT", "DEL", "GLOBAL", "NOT", "WITH", 
			"ASYNC", "ELIF", "IF", "OR", "YIELD", "PLUS", "MINUS", "STAR", "DOUBLESTAR", 
			"SLASH", "DOUBLESLASH", "PERCENT", "EQ", "NEQ", "LE", "GE", "LT", "GT", 
			"ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", 
			"DSLASH_ASSIGN", "PERCENT_ASSIGN", "POWER_ASSIGN", "AMP_ASSIGN", "PIPE_ASSIGN", 
			"CARET_ASSIGN", "RSHIFT_ASSIGN", "LSHIFT_ASSIGN", "WALRUS", "AMP", "PIPE", 
			"CARET", "TILDE", "LSHIFT", "RSHIFT", "LPAREN", "RPAREN", "LBRACKET", 
			"RBRACKET", "LBRACE", "RBRACE", "COMMA", "COLON", "DOT", "SEMI", "AT", 
			"ARROW", "ELLIPSIS", "NAME", "INT", "FLOAT", "STRING", "COMMENT", "WS", 
			"NEWLINE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PyLiteParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PyLiteParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PyLiteParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(PyLiteParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(PyLiteParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(36);
				match(NEWLINE);
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 861293650824L) != 0) || ((((_la - 71)) & ~0x3f) == 0 && ((1L << (_la - 71)) & 122881L) != 0)) {
				{
				{
				setState(42);
				statement();
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(48);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public CompoundStmtContext compoundStmt() {
			return getRuleContext(CompoundStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FALSE:
			case PASS:
			case NONE:
			case BREAK:
			case TRUE:
			case RETURN:
			case CONTINUE:
			case NOT:
			case PLUS:
			case MINUS:
			case LPAREN:
			case NAME:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				simpleStmt();
				}
				break;
			case FOR:
			case DEF:
			case WHILE:
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				compoundStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SimpleStmtContext extends ParserRuleContext {
		public List<SmallStmtContext> smallStmt() {
			return getRuleContexts(SmallStmtContext.class);
		}
		public SmallStmtContext smallStmt(int i) {
			return getRuleContext(SmallStmtContext.class,i);
		}
		public TerminalNode NEWLINE() { return getToken(PyLiteParser.NEWLINE, 0); }
		public List<TerminalNode> SEMI() { return getTokens(PyLiteParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(PyLiteParser.SEMI, i);
		}
		public SimpleStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStmt; }
	}

	public final SimpleStmtContext simpleStmt() throws RecognitionException {
		SimpleStmtContext _localctx = new SimpleStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_simpleStmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			smallStmt();
			setState(59);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(55);
					match(SEMI);
					setState(56);
					smallStmt();
					}
					} 
				}
				setState(61);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(62);
				match(SEMI);
				}
			}

			setState(65);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SmallStmtContext extends ParserRuleContext {
		public AssignStmtContext assignStmt() {
			return getRuleContext(AssignStmtContext.class,0);
		}
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public TerminalNode PASS() { return getToken(PyLiteParser.PASS, 0); }
		public TerminalNode BREAK() { return getToken(PyLiteParser.BREAK, 0); }
		public TerminalNode CONTINUE() { return getToken(PyLiteParser.CONTINUE, 0); }
		public SmallStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_smallStmt; }
	}

	public final SmallStmtContext smallStmt() throws RecognitionException {
		SmallStmtContext _localctx = new SmallStmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_smallStmt);
		try {
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(67);
				assignStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(68);
				exprStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(69);
				returnStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(70);
				match(PASS);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(71);
				match(BREAK);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(72);
				match(CONTINUE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignStmtContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(PyLiteParser.NAME, 0); }
		public AssignOpContext assignOp() {
			return getRuleContext(AssignOpContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStmt; }
	}

	public final AssignStmtContext assignStmt() throws RecognitionException {
		AssignStmtContext _localctx = new AssignStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(NAME);
			setState(76);
			assignOp();
			setState(77);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignOpContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(PyLiteParser.ASSIGN, 0); }
		public TerminalNode PLUS_ASSIGN() { return getToken(PyLiteParser.PLUS_ASSIGN, 0); }
		public TerminalNode MINUS_ASSIGN() { return getToken(PyLiteParser.MINUS_ASSIGN, 0); }
		public TerminalNode STAR_ASSIGN() { return getToken(PyLiteParser.STAR_ASSIGN, 0); }
		public TerminalNode SLASH_ASSIGN() { return getToken(PyLiteParser.SLASH_ASSIGN, 0); }
		public AssignOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignOp; }
	}

	public final AssignOpContext assignOp() throws RecognitionException {
		AssignOpContext _localctx = new AssignOpContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 69805794224242688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprStmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprStmt; }
	}

	public final ExprStmtContext exprStmt() throws RecognitionException {
		ExprStmtContext _localctx = new ExprStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_exprStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(PyLiteParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_returnStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(RETURN);
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 826781212936L) != 0) || ((((_la - 71)) & ~0x3f) == 0 && ((1L << (_la - 71)) & 122881L) != 0)) {
				{
				setState(84);
				expr(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompoundStmtContext extends ParserRuleContext {
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public FuncDefContext funcDef() {
			return getRuleContext(FuncDefContext.class,0);
		}
		public CompoundStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundStmt; }
	}

	public final CompoundStmtContext compoundStmt() throws RecognitionException {
		CompoundStmtContext _localctx = new CompoundStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_compoundStmt);
		try {
			setState(91);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				ifStmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				whileStmt();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				forStmt();
				}
				break;
			case DEF:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				funcDef();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(PyLiteParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(PyLiteParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(PyLiteParser.COLON, i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> ELIF() { return getTokens(PyLiteParser.ELIF); }
		public TerminalNode ELIF(int i) {
			return getToken(PyLiteParser.ELIF, i);
		}
		public TerminalNode ELSE() { return getToken(PyLiteParser.ELSE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(IF);
			setState(94);
			expr(0);
			setState(95);
			match(COLON);
			setState(96);
			block();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF) {
				{
				{
				setState(97);
				match(ELIF);
				setState(98);
				expr(0);
				setState(99);
				match(COLON);
				setState(100);
				block();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(107);
				match(ELSE);
				setState(108);
				match(COLON);
				setState(109);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(PyLiteParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PyLiteParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_whileStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(WHILE);
			setState(113);
			expr(0);
			setState(114);
			match(COLON);
			setState(115);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(PyLiteParser.FOR, 0); }
		public TerminalNode NAME() { return getToken(PyLiteParser.NAME, 0); }
		public TerminalNode IN() { return getToken(PyLiteParser.IN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PyLiteParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_forStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(FOR);
			setState(118);
			match(NAME);
			setState(119);
			match(IN);
			setState(120);
			expr(0);
			setState(121);
			match(COLON);
			setState(122);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncDefContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(PyLiteParser.DEF, 0); }
		public TerminalNode NAME() { return getToken(PyLiteParser.NAME, 0); }
		public TerminalNode LPAREN() { return getToken(PyLiteParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(PyLiteParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(PyLiteParser.COLON, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public FuncDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDef; }
	}

	public final FuncDefContext funcDef() throws RecognitionException {
		FuncDefContext _localctx = new FuncDefContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_funcDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(DEF);
			setState(125);
			match(NAME);
			setState(126);
			match(LPAREN);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(127);
				paramList();
				}
			}

			setState(130);
			match(RPAREN);
			setState(131);
			match(COLON);
			setState(132);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamListContext extends ParserRuleContext {
		public List<TerminalNode> NAME() { return getTokens(PyLiteParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(PyLiteParser.NAME, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PyLiteParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PyLiteParser.COMMA, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(NAME);
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(135);
				match(COMMA);
				setState(136);
				match(NAME);
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(PyLiteParser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(PyLiteParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(PyLiteParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_block);
		int _la;
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEWLINE:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				match(NEWLINE);
				setState(143);
				match(INDENT);
				setState(145); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(144);
					statement();
					}
					}
					setState(147); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 861293650824L) != 0) || ((((_la - 71)) & ~0x3f) == 0 && ((1L << (_la - 71)) & 122881L) != 0) );
				setState(149);
				match(DEDENT);
				}
				break;
			case FALSE:
			case PASS:
			case NONE:
			case BREAK:
			case TRUE:
			case RETURN:
			case CONTINUE:
			case NOT:
			case PLUS:
			case MINUS:
			case LPAREN:
			case NAME:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				simpleStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IndexExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LBRACKET() { return getToken(PyLiteParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(PyLiteParser.RBRACKET, 0); }
		public IndexExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(PyLiteParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PyLiteParser.MINUS, 0); }
		public UnaryExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotExprContext extends ExprContext {
		public TerminalNode NOT() { return getToken(PyLiteParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PowerExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(PyLiteParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(PyLiteParser.STAR, i);
		}
		public PowerExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(PyLiteParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PyLiteParser.MINUS, 0); }
		public AddExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode STAR() { return getToken(PyLiteParser.STAR, 0); }
		public TerminalNode SLASH() { return getToken(PyLiteParser.SLASH, 0); }
		public TerminalNode DOUBLESLASH() { return getToken(PyLiteParser.DOUBLESLASH, 0); }
		public TerminalNode PERCENT() { return getToken(PyLiteParser.PERCENT, 0); }
		public MulExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomExprContext extends ExprContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public AtomExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OR() { return getToken(PyLiteParser.OR, 0); }
		public OrExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CallExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(PyLiteParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(PyLiteParser.RPAREN, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public CallExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompareExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(PyLiteParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(PyLiteParser.NEQ, 0); }
		public TerminalNode LT() { return getToken(PyLiteParser.LT, 0); }
		public TerminalNode GT() { return getToken(PyLiteParser.GT, 0); }
		public TerminalNode LE() { return getToken(PyLiteParser.LE, 0); }
		public TerminalNode GE() { return getToken(PyLiteParser.GE, 0); }
		public CompareExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode AND() { return getToken(PyLiteParser.AND, 0); }
		public AndExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
				{
				_localctx = new UnaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(155);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(156);
				expr(8);
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(157);
				match(NOT);
				setState(158);
				expr(4);
				}
				break;
			case FALSE:
			case NONE:
			case TRUE:
			case LPAREN:
			case NAME:
			case INT:
			case FLOAT:
			case STRING:
				{
				_localctx = new AtomExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(159);
				atom();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(194);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(192);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new PowerExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(162);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(163);
						match(STAR);
						setState(164);
						match(STAR);
						setState(165);
						expr(9);
						}
						break;
					case 2:
						{
						_localctx = new MulExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(167);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 31885837205504L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(168);
						expr(8);
						}
						break;
					case 3:
						{
						_localctx = new AddExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(169);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(170);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(171);
						expr(7);
						}
						break;
					case 4:
						{
						_localctx = new CompareExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(172);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(173);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2216615441596416L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(174);
						expr(6);
						}
						break;
					case 5:
						{
						_localctx = new AndExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(175);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(176);
						match(AND);
						setState(177);
						expr(4);
						}
						break;
					case 6:
						{
						_localctx = new OrExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(178);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(179);
						match(OR);
						setState(180);
						expr(3);
						}
						break;
					case 7:
						{
						_localctx = new CallExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(181);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(182);
						match(LPAREN);
						setState(184);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 826781212936L) != 0) || ((((_la - 71)) & ~0x3f) == 0 && ((1L << (_la - 71)) & 122881L) != 0)) {
							{
							setState(183);
							argList();
							}
						}

						setState(186);
						match(RPAREN);
						}
						break;
					case 8:
						{
						_localctx = new IndexExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(187);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(188);
						match(LBRACKET);
						setState(189);
						expr(0);
						setState(190);
						match(RBRACKET);
						}
						break;
					}
					} 
				}
				setState(196);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PyLiteParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PyLiteParser.COMMA, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			expr(0);
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(198);
				match(COMMA);
				setState(199);
				expr(0);
				}
				}
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	 
		public AtomContext() { }
		public void copyFrom(AtomContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NameAtomContext extends AtomContext {
		public TerminalNode NAME() { return getToken(PyLiteParser.NAME, 0); }
		public NameAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NoneAtomContext extends AtomContext {
		public TerminalNode NONE() { return getToken(PyLiteParser.NONE, 0); }
		public NoneAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatAtomContext extends AtomContext {
		public TerminalNode FLOAT() { return getToken(PyLiteParser.FLOAT, 0); }
		public FloatAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenAtomContext extends AtomContext {
		public TerminalNode LPAREN() { return getToken(PyLiteParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PyLiteParser.RPAREN, 0); }
		public ParenAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntAtomContext extends AtomContext {
		public TerminalNode INT() { return getToken(PyLiteParser.INT, 0); }
		public IntAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringAtomContext extends AtomContext {
		public TerminalNode STRING() { return getToken(PyLiteParser.STRING, 0); }
		public StringAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FalseAtomContext extends AtomContext {
		public TerminalNode FALSE() { return getToken(PyLiteParser.FALSE, 0); }
		public FalseAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TrueAtomContext extends AtomContext {
		public TerminalNode TRUE() { return getToken(PyLiteParser.TRUE, 0); }
		public TrueAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_atom);
		try {
			setState(216);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				_localctx = new NameAtomContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(NAME);
				}
				break;
			case INT:
				_localctx = new IntAtomContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(INT);
				}
				break;
			case FLOAT:
				_localctx = new FloatAtomContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(207);
				match(FLOAT);
				}
				break;
			case STRING:
				_localctx = new StringAtomContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(208);
				match(STRING);
				}
				break;
			case TRUE:
				_localctx = new TrueAtomContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(209);
				match(TRUE);
				}
				break;
			case FALSE:
				_localctx = new FalseAtomContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(210);
				match(FALSE);
				}
				break;
			case NONE:
				_localctx = new NoneAtomContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(211);
				match(NONE);
				}
				break;
			case LPAREN:
				_localctx = new ParenAtomContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(212);
				match(LPAREN);
				setState(213);
				expr(0);
				setState(214);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		case 6:
			return precpred(_ctx, 11);
		case 7:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001Z\u00db\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0005\u0000"+
		"&\b\u0000\n\u0000\f\u0000)\t\u0000\u0001\u0000\u0005\u0000,\b\u0000\n"+
		"\u0000\f\u0000/\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0003\u00015\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002"+
		":\b\u0002\n\u0002\f\u0002=\t\u0002\u0001\u0002\u0003\u0002@\b\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003J\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0003\u0007V\b\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\b\\\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0005\tg\b\t\n\t\f\tj\t\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\to\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0003\f\u0081\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u008a\b\r\n\r\f\r\u008d\t\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0004\u000e\u0092\b\u000e\u000b\u000e\f\u000e\u0093"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0099\b\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00a1\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00b9\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0005\u000f\u00c1\b\u000f\n\u000f\f\u000f\u00c4\t\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00c9\b\u0010\n\u0010\f\u0010"+
		"\u00cc\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0003\u0011\u00d9\b\u0011\u0001\u0011\u0000\u0001\u001e\u0012\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"\u0000\u0004\u0001\u000037\u0001\u0000&\'\u0002\u0000((*,\u0001\u0000"+
		"-2\u00ef\u0000\'\u0001\u0000\u0000\u0000\u00024\u0001\u0000\u0000\u0000"+
		"\u00046\u0001\u0000\u0000\u0000\u0006I\u0001\u0000\u0000\u0000\bK\u0001"+
		"\u0000\u0000\u0000\nO\u0001\u0000\u0000\u0000\fQ\u0001\u0000\u0000\u0000"+
		"\u000eS\u0001\u0000\u0000\u0000\u0010[\u0001\u0000\u0000\u0000\u0012]"+
		"\u0001\u0000\u0000\u0000\u0014p\u0001\u0000\u0000\u0000\u0016u\u0001\u0000"+
		"\u0000\u0000\u0018|\u0001\u0000\u0000\u0000\u001a\u0086\u0001\u0000\u0000"+
		"\u0000\u001c\u0098\u0001\u0000\u0000\u0000\u001e\u00a0\u0001\u0000\u0000"+
		"\u0000 \u00c5\u0001\u0000\u0000\u0000\"\u00d8\u0001\u0000\u0000\u0000"+
		"$&\u0005Z\u0000\u0000%$\u0001\u0000\u0000\u0000&)\u0001\u0000\u0000\u0000"+
		"\'%\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000\u0000(-\u0001\u0000\u0000"+
		"\u0000)\'\u0001\u0000\u0000\u0000*,\u0003\u0002\u0001\u0000+*\u0001\u0000"+
		"\u0000\u0000,/\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001"+
		"\u0000\u0000\u0000.0\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000"+
		"01\u0005\u0000\u0000\u00011\u0001\u0001\u0000\u0000\u000025\u0003\u0004"+
		"\u0002\u000035\u0003\u0010\b\u000042\u0001\u0000\u0000\u000043\u0001\u0000"+
		"\u0000\u00005\u0003\u0001\u0000\u0000\u00006;\u0003\u0006\u0003\u0000"+
		"78\u0005P\u0000\u00008:\u0003\u0006\u0003\u000097\u0001\u0000\u0000\u0000"+
		":=\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000"+
		"\u0000<?\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000>@\u0005P\u0000"+
		"\u0000?>\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@A\u0001\u0000"+
		"\u0000\u0000AB\u0005Z\u0000\u0000B\u0005\u0001\u0000\u0000\u0000CJ\u0003"+
		"\b\u0004\u0000DJ\u0003\f\u0006\u0000EJ\u0003\u000e\u0007\u0000FJ\u0005"+
		"\u0007\u0000\u0000GJ\u0005\t\u0000\u0000HJ\u0005\u0013\u0000\u0000IC\u0001"+
		"\u0000\u0000\u0000ID\u0001\u0000\u0000\u0000IE\u0001\u0000\u0000\u0000"+
		"IF\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000"+
		"\u0000J\u0007\u0001\u0000\u0000\u0000KL\u0005T\u0000\u0000LM\u0003\n\u0005"+
		"\u0000MN\u0003\u001e\u000f\u0000N\t\u0001\u0000\u0000\u0000OP\u0007\u0000"+
		"\u0000\u0000P\u000b\u0001\u0000\u0000\u0000QR\u0003\u001e\u000f\u0000"+
		"R\r\u0001\u0000\u0000\u0000SU\u0005\u0011\u0000\u0000TV\u0003\u001e\u000f"+
		"\u0000UT\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000V\u000f\u0001"+
		"\u0000\u0000\u0000W\\\u0003\u0012\t\u0000X\\\u0003\u0014\n\u0000Y\\\u0003"+
		"\u0016\u000b\u0000Z\\\u0003\u0018\f\u0000[W\u0001\u0000\u0000\u0000[X"+
		"\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[Z\u0001\u0000\u0000"+
		"\u0000\\\u0011\u0001\u0000\u0000\u0000]^\u0005#\u0000\u0000^_\u0003\u001e"+
		"\u000f\u0000_`\u0005N\u0000\u0000`h\u0003\u001c\u000e\u0000ab\u0005\""+
		"\u0000\u0000bc\u0003\u001e\u000f\u0000cd\u0005N\u0000\u0000de\u0003\u001c"+
		"\u000e\u0000eg\u0001\u0000\u0000\u0000fa\u0001\u0000\u0000\u0000gj\u0001"+
		"\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000"+
		"in\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000kl\u0005\u0005\u0000"+
		"\u0000lm\u0005N\u0000\u0000mo\u0003\u001c\u000e\u0000nk\u0001\u0000\u0000"+
		"\u0000no\u0001\u0000\u0000\u0000o\u0013\u0001\u0000\u0000\u0000pq\u0005"+
		"\u001b\u0000\u0000qr\u0003\u001e\u000f\u0000rs\u0005N\u0000\u0000st\u0003"+
		"\u001c\u000e\u0000t\u0015\u0001\u0000\u0000\u0000uv\u0005\u0014\u0000"+
		"\u0000vw\u0005T\u0000\u0000wx\u0005\u000b\u0000\u0000xy\u0003\u001e\u000f"+
		"\u0000yz\u0005N\u0000\u0000z{\u0003\u001c\u000e\u0000{\u0017\u0001\u0000"+
		"\u0000\u0000|}\u0005\u0018\u0000\u0000}~\u0005T\u0000\u0000~\u0080\u0005"+
		"G\u0000\u0000\u007f\u0081\u0003\u001a\r\u0000\u0080\u007f\u0001\u0000"+
		"\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0005H\u0000\u0000\u0083\u0084\u0005N\u0000\u0000"+
		"\u0084\u0085\u0003\u001c\u000e\u0000\u0085\u0019\u0001\u0000\u0000\u0000"+
		"\u0086\u008b\u0005T\u0000\u0000\u0087\u0088\u0005M\u0000\u0000\u0088\u008a"+
		"\u0005T\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008d\u0001"+
		"\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001"+
		"\u0000\u0000\u0000\u008c\u001b\u0001\u0000\u0000\u0000\u008d\u008b\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0005Z\u0000\u0000\u008f\u0091\u0005\u0001"+
		"\u0000\u0000\u0090\u0092\u0003\u0002\u0001\u0000\u0091\u0090\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000"+
		"\u0000\u0000\u0095\u0096\u0005\u0002\u0000\u0000\u0096\u0099\u0001\u0000"+
		"\u0000\u0000\u0097\u0099\u0003\u0004\u0002\u0000\u0098\u008e\u0001\u0000"+
		"\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0099\u001d\u0001\u0000"+
		"\u0000\u0000\u009a\u009b\u0006\u000f\uffff\uffff\u0000\u009b\u009c\u0007"+
		"\u0001\u0000\u0000\u009c\u00a1\u0003\u001e\u000f\b\u009d\u009e\u0005\u001f"+
		"\u0000\u0000\u009e\u00a1\u0003\u001e\u000f\u0004\u009f\u00a1\u0003\"\u0011"+
		"\u0000\u00a0\u009a\u0001\u0000\u0000\u0000\u00a0\u009d\u0001\u0000\u0000"+
		"\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u00c2\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\n\t\u0000\u0000\u00a3\u00a4\u0005(\u0000\u0000\u00a4"+
		"\u00a5\u0005(\u0000\u0000\u00a5\u00c1\u0003\u001e\u000f\t\u00a6\u00a7"+
		"\n\u0007\u0000\u0000\u00a7\u00a8\u0007\u0002\u0000\u0000\u00a8\u00c1\u0003"+
		"\u001e\u000f\b\u00a9\u00aa\n\u0006\u0000\u0000\u00aa\u00ab\u0007\u0001"+
		"\u0000\u0000\u00ab\u00c1\u0003\u001e\u000f\u0007\u00ac\u00ad\n\u0005\u0000"+
		"\u0000\u00ad\u00ae\u0007\u0003\u0000\u0000\u00ae\u00c1\u0003\u001e\u000f"+
		"\u0006\u00af\u00b0\n\u0003\u0000\u0000\u00b0\u00b1\u0005\u0012\u0000\u0000"+
		"\u00b1\u00c1\u0003\u001e\u000f\u0004\u00b2\u00b3\n\u0002\u0000\u0000\u00b3"+
		"\u00b4\u0005$\u0000\u0000\u00b4\u00c1\u0003\u001e\u000f\u0003\u00b5\u00b6"+
		"\n\u000b\u0000\u0000\u00b6\u00b8\u0005G\u0000\u0000\u00b7\u00b9\u0003"+
		" \u0010\u0000\u00b8\u00b7\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000"+
		"\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00c1\u0005H\u0000"+
		"\u0000\u00bb\u00bc\n\n\u0000\u0000\u00bc\u00bd\u0005I\u0000\u0000\u00bd"+
		"\u00be\u0003\u001e\u000f\u0000\u00be\u00bf\u0005J\u0000\u0000\u00bf\u00c1"+
		"\u0001\u0000\u0000\u0000\u00c0\u00a2\u0001\u0000\u0000\u0000\u00c0\u00a6"+
		"\u0001\u0000\u0000\u0000\u00c0\u00a9\u0001\u0000\u0000\u0000\u00c0\u00ac"+
		"\u0001\u0000\u0000\u0000\u00c0\u00af\u0001\u0000\u0000\u0000\u00c0\u00b2"+
		"\u0001\u0000\u0000\u0000\u00c0\u00b5\u0001\u0000\u0000\u0000\u00c0\u00bb"+
		"\u0001\u0000\u0000\u0000\u00c1\u00c4\u0001\u0000\u0000\u0000\u00c2\u00c0"+
		"\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000\u0000\u00c3\u001f"+
		"\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c5\u00ca"+
		"\u0003\u001e\u000f\u0000\u00c6\u00c7\u0005M\u0000\u0000\u00c7\u00c9\u0003"+
		"\u001e\u000f\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9\u00cc\u0001"+
		"\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca\u00cb\u0001"+
		"\u0000\u0000\u0000\u00cb!\u0001\u0000\u0000\u0000\u00cc\u00ca\u0001\u0000"+
		"\u0000\u0000\u00cd\u00d9\u0005T\u0000\u0000\u00ce\u00d9\u0005U\u0000\u0000"+
		"\u00cf\u00d9\u0005V\u0000\u0000\u00d0\u00d9\u0005W\u0000\u0000\u00d1\u00d9"+
		"\u0005\r\u0000\u0000\u00d2\u00d9\u0005\u0003\u0000\u0000\u00d3\u00d9\u0005"+
		"\b\u0000\u0000\u00d4\u00d5\u0005G\u0000\u0000\u00d5\u00d6\u0003\u001e"+
		"\u000f\u0000\u00d6\u00d7\u0005H\u0000\u0000\u00d7\u00d9\u0001\u0000\u0000"+
		"\u0000\u00d8\u00cd\u0001\u0000\u0000\u0000\u00d8\u00ce\u0001\u0000\u0000"+
		"\u0000\u00d8\u00cf\u0001\u0000\u0000\u0000\u00d8\u00d0\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d1\u0001\u0000\u0000\u0000\u00d8\u00d2\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d3\u0001\u0000\u0000\u0000\u00d8\u00d4\u0001\u0000\u0000"+
		"\u0000\u00d9#\u0001\u0000\u0000\u0000\u0014\'-4;?IU[hn\u0080\u008b\u0093"+
		"\u0098\u00a0\u00b8\u00c0\u00c2\u00ca\u00d8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}