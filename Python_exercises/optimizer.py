from typing import Optional
from tree import Node, Var, Val, Op, OpSym
from ast import NodeTransformer
from parser import parse
import ast


def node_to_str(tree: Node) -> str:
    """Takes a tree and returns it as a string"""
    tree_str = ""
    match tree:
        case Op(OpSym, left, right):
            tree_str += "(" + \
                node_to_str(left) + \
                " " + str(OpSym.value) + " " +\
                node_to_str(right) + ")"
        case Val(i):
            tree_str += str(i)
        case Var(x):
            tree_str += x
        case _:
            raise Exception("unreachable")
    return str(tree_str)


def node_to_str_if(tree: Node) -> str:
    """Uses if clauses to turn a tree into a string."""
    tree_str = ""
    if isinstance(tree, Op):
        tree_str += "(" +\
            node_to_str_if(tree.left) +\
            " " + str(tree.sym.value) + " " +\
            node_to_str_if(tree.right) + ")"
    elif isinstance(tree, Var):
        tree_str += str(tree.name)
    elif isinstance(tree, Val):
        tree_str += str(tree.value)
    return tree_str


def optimize_step(e: Optional[Node]) -> Optional[Node]:
    """Takes a tree and uses pattern matching to rearrange it according to set rules, returning None if no rule applies."""
    match e:
        case Op(o, Val(v1), Val(v2)):
            if e.sym == OpSym.MUL:
                return Val(v1 * v2)
            elif e.sym == OpSym.ADD:
                return Val(v1 + v2)

        case Op(o, e1, e2) if e1==e2:
            return Op(OpSym.MUL, Val(2), e1)

        case Op(o1, e1, Op(o2, e2, e3)) if o1 == o2:
            return Op(o1, Op(o2, e1, e2), e3)

        case Op(o, e1, e2):
            e1_opt = optimize_step(e1)
            if e1_opt is not None:
                return Op(o, e1_opt, e2)
            e2_opt = optimize_step(e2)
            if e2_opt is not None:
                return Op(o, e1, e2_opt)
            return None

        case _:
            return None


#def optimize_step_if(e: Optional[Node]) -> Optional[Node]:
   # """Takes a tree and uses if clauses to rearrange it according to set rules, returning None if no rule applies."""
   # if isinstance(e.left, Val) and isinstance(e.right, Val):
   #     if e.sym == OpSym.MUL:
   #         result = Val(e.left.value * e.right.value)
   #     elif e.sym == OpSym.ADD:
   #         result = Val(left.value + right.value)
   #     return result
   # elif e.sym == OpSym.ADD and e.left == e.right:
   #     return Op(OpSym.MUL, Val(2), e.left)
    # elif e == Op(OpSym, left=Op, right=e):
   #     left_tree = optimize_step(e.left)
   #     return Op(OpSym, left_tree, e.right)
    # elif e == Op(OpSym, left=e, right = Op):
   #     right_tree = optimize_step(e.right)
   #     return Op(OpSym, e.left, right_tree)
   # return None



def optimize(e: Optional[Node]) -> list:
    """Applies the optimize_step function to rearrange the tree until no more rules apply
    and then returns a list of the results, including e."""
    result = [e]
    while optimize_step(e) is not None:
        result += [optimize_step(e)]
    return result


if __name__ == "__main__":
    e1 = Op(OpSym.MUL, Val(2), Val(3)) 
    e2 = Op(OpSym.MUL, Val(3), Val(2)) 
    assert optimize_step(Op(OpSym.ADD, e1, e2)) == Op(OpSym.ADD, Val(6), e2) 
    assert optimize_step(Op(OpSym.ADD, Val(6), e2)) == Op(OpSym.ADD, Val(6), Val(6)) 
    assert optimize_step(Op(OpSym.ADD, Val(6), Val(6))) == Val(12) 
    assert optimize_step(Val(12)) == None
    assert optimize(parse('(x + x) + (x + x)')) == [ parse('(x + x) + (x + x)'), parse('(2 * (x + x))'), parse('(2 * (2 * x))'), parse('((2 * 2) * x)'), parse('(4 * x)') ]


#if __name__ == "__main__":
    #parse()
    #optimize()
    #node_to_str()